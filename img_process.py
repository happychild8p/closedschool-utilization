#!/usr/bin/python3

import cv2
import numpy as np
import matplotlib.pyplot as plt
import re
import matplotlib.font_manager as fm
import pandas as pd

def get_features():
    features = ["agricultural_area","central_commercial_area","commercial_area","green_area",
            "highway","industrial_area","management_area","mountains","nature_reserved_area"
            ,"reserved_residential","residential_area","road","semi_residential_area",
            "water"]
    imglist = []
    for idx in range(len(features)):
        img_path = f'map_rgb_params/{features[idx]}.png'
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        imglist.append(img[1][1])       
    features_dict = dict(zip(features, imglist))
    return features_dict

def get_data():
    f = open('C:/Users/Heedong/testset/names2.txt','rt', encoding='utf-8')  
    names = f.read().split("\n")
    names_refined = []
    pathes = []
    for path in names:
        path = re.sub("\s","", path)
        pathes.append(f'C:/Users/Heedong/testset/{path}')
        names_refined.append(path.strip('.png'))
    f.close() 
    datalist = []   ### opencv 한글경로 깨짐 문제 해결
    for path in pathes:
        stream = open(path.encode("utf-8"), 'rb')
        tmpBytes = bytearray(stream.read())
        npArray = np.asarray(tmpBytes, dtype=np.uint8)
        datalist.append(cv2.imdecode(npArray, cv2.IMREAD_UNCHANGED))
    return datalist, names_refined
    #return cv2.imdecode(npArray, cv2.IMREAD_UNCHANGED)
def get_data_usage():
    f = open('C:/Users/Heedong/testset/names_usage.txt','rt', encoding='utf-8')
    li=[]; usage_dict = {}
    for each in f.read().split("\n"): li.append(each.split(','))
    for each in li[:-3]: usage_dict[each[0].strip('.png')] = each[1]
    f.close()
    return usage_dict
    
def get_test(filepath):
    stream = open(filepath.encode("utf-8"), 'rb')
    tmpBytes = bytearray(stream.read())
    npArray = np.asarray(tmpBytes, dtype=np.uint8)
    test = cv2.imdecode(npArray, cv2.IMREAD_UNCHANGED)
    return test

def np_hist_to_cv(np_histogram_output):
    counts, bin_edges = np_histogram_output
    return counts.ravel().astype('float32')

def histogram_matching_flatten(dataList, names, test, nbins):
    imsif = test.flatten()
    drop_transparency = input("Do you want to remove transparency?[y/n] ")
    if drop_transparency.lower() == 'y':
        zfill = np.zeros(4077118)
        imsif[4077118*3:] = zfill
        #imsi = imsif.reshape(1453,2806,-1)
    h1f = np.histogram(imsif, bins=nbins)
    values = []    
    for i in range(len(dataList)):
        sub_val = []
        data = dataList[i].flatten()
        if drop_transparency.lower() == 'y': 
            data[4077118*3:] = zfill
        h2f = np.histogram(data, bins=nbins)
        sub_val.append(round(cv2.compareHist(np_hist_to_cv(h1f), np_hist_to_cv(h2f), cv2.HISTCMP_CORREL), 5))
        sub_val.append(round(cv2.compareHist(np_hist_to_cv(h1f), np_hist_to_cv(h2f), cv2.HISTCMP_CHISQR), 5))
        sub_val.append(round(cv2.compareHist(np_hist_to_cv(h1f), np_hist_to_cv(h2f), cv2.HISTCMP_INTERSECT), 5))
        sub_val.append(round(cv2.compareHist(np_hist_to_cv(h1f), np_hist_to_cv(h2f), cv2.HISTCMP_BHATTACHARYYA), 5))
        values.append(sub_val)
    return dict(zip(names, values)) 

def histogram_matching_unflatten(dataList, names, test, nbins):
    imsi = test
    drop_transparency = input("Do you want to remove transparency?[y/n] ")
    if drop_transparency.lower() == 'y':
        imsif = imsi.flatten()
        zfill = np.zeros(4077118)
        imsif[4077118*3:] = zfill
        imsi = imsif.reshape(1453,2806,-1)
    h1 = np.histogram(imsi, bins=nbins)
    values = []    
    for i in range(len(dataList)):
        sub_val = []
        data = dataList[i]
        if drop_transparency.lower() == 'y': 
            dataf = data.flatten()
            dataf[4077118*3:] = zfill
            data = dataf.reshape(1453,2806,-1)
        h2 = np.histogram(data, bins=nbins)
        sub_val.append(round(cv2.compareHist(np_hist_to_cv(h1), np_hist_to_cv(h2), cv2.HISTCMP_CORREL), 5))
        sub_val.append(round(cv2.compareHist(np_hist_to_cv(h1), np_hist_to_cv(h2), cv2.HISTCMP_CHISQR), 5))
        sub_val.append(round(cv2.compareHist(np_hist_to_cv(h1), np_hist_to_cv(h2), cv2.HISTCMP_INTERSECT), 5))
        sub_val.append(round(cv2.compareHist(np_hist_to_cv(h1), np_hist_to_cv(h2), cv2.HISTCMP_BHATTACHARYYA), 5))
        values.append(sub_val)
    return dict(zip(names, values))

def get_idxlist(result_dict, nums):
    correlation = []; chi_square = []; intersection = []; bhattacharyya = [];
    for name in names:
        correlation.append(result_dict[name][0])
        chi_square.append(result_dict[name][1])
        intersection.append(result_dict[name][2])
        bhattacharyya.append(result_dict[name][3])
    
    cormax = []; chimin = []; intermax = []; bhattmin = []
    for i in range(nums):
        cormax.append(correlation.index(max(correlation)))
        chimin.append(chi_square.index(min(chi_square)))
        intermax.append(intersection.index(max(intersection)))
        bhattmin.append(bhattacharyya.index(min(bhattacharyya)))
        
        correlation.remove(max(correlation))
        chi_square.remove(min(chi_square))
        intersection.remove(max(intersection))
        bhattacharyya.remove(min(bhattacharyya))
        
    return cormax, chimin, intermax, bhattmin

def show_img(dataList, names, cormax, chimin, intermax, bhattmin):   
    rows = len(cormax); cols = 4
    axes=[]
    fig=plt.figure()
    for row in range(rows):
        axes.append(fig.add_subplot(rows, cols, (row*4)+1))
        subplot_title=(f"Correlation\n{names[cormax[row]]}")
        axes[-1].set_title(subplot_title)  
        plt.imshow(dataList[cormax[row]])
        
        axes.append(fig.add_subplot(rows, cols, (row*4)+2))
        subplot_title=(f"chi-square\n{names[chimin[row]]}")
        axes[-1].set_title(subplot_title)  
        plt.imshow(dataList[chimin[row]])
                
        axes.append(fig.add_subplot(rows, cols, (row*4)+3))
        subplot_title=(f"intermax\n{names[intermax[row]]}")
        axes[-1].set_title(subplot_title)  
        plt.imshow(dataList[intermax[row]])
        
        axes.append(fig.add_subplot(rows, cols, (row*4)+4))
        subplot_title=(f"bhattmin\n{names[bhattmin[row]]}")
        axes[-1].set_title(subplot_title)  
        plt.imshow(dataList[bhattmin[row]])
    fig.tight_layout()    
    plt.show()
    
def show_usage(names, cormax, chimin, intermax, bhattmin):
    usage_set = set()
    for i in range(len(cormax)):
        usage_set.add(names[cormax[i]])
        usage_set.add(names[chimin[i]])
        usage_set.add(names[intermax[i]])
        usage_set.add(names[bhattmin[i]])
    for i in range(len(usage_set)): print(list(usage_set)[i],':', usage_dict[list(usage_set)[i]])

def get_color_histogram(image):
    testt = cv2.cvtColor(dataList[30], cv2.COLOR_BGR2RGB)
    r = np.array(testt)[:,:,0].flatten()
    g = np.array(testt)[:,:,1].flatten()
    b = np.array(testt)[:,:,2].flatten()

    bins_range = range(0, 257, 4) 
    # x tic값 범위 설정
    xtics_range = range(0, 257, 32)
 
    # Ver1 : RGB 한번에 그리기 (subplot 이용)
    fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=False)
 
    ax0.hist(r, bins=bins_range, color='r')
    ax1.hist(g, bins=bins_range, color='g')
    ax2.hist(b, bins=bins_range, color='b')
 
    ax0.grid(True)
    ax1.grid(True)
    ax2.grid(True)
 
    plt.setp((ax0, ax1, ax2), xticks=xtics_range, xlim=(0, 256))
    plt.show()
    
if __name__ == "__main__":
    path_to_font = "C:/Windows/Fonts/H2GTRM.ttf"
    font_name = fm.FontProperties(fname=path_to_font).get_name()
    plt.rc('font', family=font_name)
    
    dataList, names = get_data()
    test = get_test("jubong.png")
    usage_dict = get_data_usage()
    plt.imshow(test)
    
    result_dict = histogram_matching_flatten(dataList, names, test, nbins=64)
    #result_dict = histogram_matching_unflatten(dataList, names, test, 64)
    cormax, chimin, intermax, bhattmin = get_idxlist(result_dict, nums=2)
    show_img(dataList, names, cormax, chimin, intermax, bhattmin)
    show_usage(names, cormax, chimin, intermax, bhattmin)
    
###기타 정보   
    imsidict = {}
    imsidict["correlation"] = [names[cormax[0]], names[cormax[1]]]
    imsidict["chi-square"] = [names[chimin[0]], names[chimin[1]]]
    imsidict["intersection"] = [names[intermax[0]], names[intermax[1]]]
    imsidict["bhattacharyya"] = [names[bhattmin[0]], names[bhattmin[1]]]
    
    get_color_histogram(dataList[30])
    print(imsidict)
    pd.DataFrame(imsidict, index=False)
    dcc = {}
    for i in ['강포초', '무주동초', '영북초', '양곡초귀산분교']: dcc[i] = result_dict[i]
    pd.DataFrame(dcc)              
       
