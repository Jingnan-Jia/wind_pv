# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 10:20:10 2020
@author: jjia
"""

from pylab import plot, show, savefig, xlim, figure, ylim, yscale, legend, boxplot, setp, axes
import matplotlib.pyplot as plt
import numpy as np
import csv
import statistics as st
import pandas as pd
#-----------------------------------
# parameters need to be changed
handle_range_value = 'average'  # or '2_points'  # change this value to select different methods for range_value
file_name = '../data/on_off_year.csv'#改文件名称 dd_geared_year.csv  on_off_year.csv pv_year.csv
year_range = [2016,2100] # 更改年份范围即可画对应年份范围的图,此处最大值设为2070, 不指定年份的话就写None。
dpi = 600 #改分辨率
#-----------------------------------
cgray = '#696969' #更改边框-须颜色
cmedians = '#696969' #中位数颜色
# function for setting the colors of the box plots pairs
def setBoxColors_1(bp, color): 
    c1, c2 = color
    setp (bp['boxes'][0], color=cgray)
    setp (bp['caps'][0], color=cgray)
    setp (bp['caps'][1], color=cgray)

    setp (bp['whiskers'][0], color=cgray)
    setp (bp['whiskers'][1], color=cgray)
    setp (bp['fliers'][0], color=cgray)
    setp (bp['fliers'][1], color=cgray)
    setp (bp['medians'][0], color=cmedians)

    setp (bp['boxes'][1], color=cgray)
    setp (bp['caps'][2], color=cgray)
    setp (bp['caps'][3], color=cgray)
    setp (bp['whiskers'][2], color=cgray)
    setp (bp['whiskers'][3], color=cgray)
    # setp(bp['fliers'][2], color='c2)
    # setp(bp['fliers'][3], color='c2')
    setp (bp['medians'][1], color=cmedians)
    bp['boxes'][0].set(facecolor=c1)  
    bp['boxes'][1].set(facecolor=c2)  
def setBoxColors(bp, color):
    plt.setp(bp['boxes'], color=cgray)
    plt.setp(bp['whiskers'], color=cgray)
    plt.setp(bp['caps'], color=cgray)
    plt.setp(bp['medians'], color=color)

def setBoxColors_3(bp, color):
    c1, c2, c3 = color
    setp (bp['boxes'][0], color=cgray)
    setp (bp['caps'][0], color=cgray)
    setp (bp['caps'][1], color=cgray)
    setp (bp['whiskers'][0], color=cgray)
    setp (bp['whiskers'][1], color=cgray)
    setp (bp['fliers'][0], color=cgray)
    setp (bp['fliers'][1], color=cgray)
    setp (bp['medians'][0], color=cmedians)
    bp['boxes'][0].set(facecolor=c1)  
    setp (bp['boxes'][1], color=cgray)
    setp (bp['caps'][2], color=cgray)
    setp (bp['caps'][3], color=cgray)
    setp (bp['whiskers'][2], color=cgray)
    setp (bp['whiskers'][3], color=cgray)
    setp(bp['fliers'][2], color=cgray)
    # setp(bp['fliers'][3], color=c2)
    setp (bp['medians'][1], color=cmedians)
    bp['boxes'][1].set(facecolor=c2) 
    setp (bp['boxes'][2], color=cgray)
    setp (bp['caps'][4], color=cgray)
    setp (bp['caps'][5], color=cgray)
    setp (bp['whiskers'][4], color=cgray)
    setp (bp['whiskers'][5], color=cgray)
    # setp(bp['fliers'][4], color=c3)
    # setp(bp['fliers'][5], color=c3)
    setp (bp['medians'][2], color=cmedians)
    bp['boxes'][2].set(facecolor=c3) 
     
    
def setBoxColors_5(bp, color):
    c1, c2, c3, c4, c5 = color
    
    setp (bp['boxes'][0], color=cgray)
    setp (bp['caps'][0], color=cgray)
    setp (bp['caps'][1], color=cgray)
    setp (bp['whiskers'][0], color=cgray)
    setp (bp['whiskers'][1], color=cgray)
    setp (bp['fliers'][0], color=cgray)
    setp (bp['fliers'][1], color=cgray)
    setp (bp['medians'][0], color=cmedians)
    bp['boxes'][0].set(facecolor=c1)  


    setp (bp['boxes'][1], color=cgray)
    setp (bp['caps'][2], color=cgray)
    setp (bp['caps'][3], color=cgray)
    setp (bp['whiskers'][2], color=cgray)
    setp (bp['whiskers'][3], color=cgray)
    setp(bp['fliers'][2], color=cgray)
    setp(bp['fliers'][3], color='red')
    setp (bp['medians'][1], color=cmedians)
    bp['boxes'][1].set(facecolor=c2)  


    setp (bp['boxes'][2], color=cgray)
    setp (bp['caps'][4], color=cgray)
    setp (bp['caps'][5], color=cgray)
    setp (bp['whiskers'][4], color=cgray)
    setp (bp['whiskers'][5], color=cgray)
    setp(bp['fliers'][4], color='green')
    #setp(bp['fliers'][5], color='green')
    setp (bp['medians'][2], color=cmedians)
    bp['boxes'][2].set(facecolor=c3)  
  

#    
    setp (bp['boxes'][3], color=cgray)
    setp (bp['caps'][6], color=cgray)
    setp (bp['caps'][7], color=cgray)
    setp (bp['whiskers'][6], color=cgray)
    setp (bp['whiskers'][7], color=cgray)
    # setp(bp['fliers'][4], color='green')
    # setp(bp['fliers'][5], color='green')
    setp (bp['medians'][3], color=cmedians)
    bp['boxes'][3].set(facecolor=c4)  


#    
    setp (bp['boxes'][4], color=cgray)
    setp (bp['caps'][8], color=cgray)
    setp (bp['caps'][9], color=cgray)
    setp (bp['whiskers'][8], color=cgray)
    setp (bp['whiskers'][9], color=cgray)
    # setp(bp['fliers'][4], color='green')
    # setp(bp['fliers'][5], color='green')
    setp (bp['medians'][4], color=cmedians)
    bp['boxes'][4].set(facecolor=c5)  

def correct_ave(data):
    """
    得到抛去异常点之后的均值。
    """
      
    #print(data)
    
    data_np = np.array(data)
    q3 = np.percentile(data_np, 75)
    q1 = np.percentile(data_np, 25)
    qr = q3 - q1
    #print('q1, q3, qr')
    #print(q1, q3, qr)
    
    up_edge = q3 + qr * 1.5 
    down_edge = q1 - qr * 1.5
    corrected_data = []
    for i in data:
        #print('i:',i)
        if (i<=up_edge) and (i>=down_edge):
            corrected_data.append(i)
            
    ave_corrected = st.mean(corrected_data)
    #print('ave_c', ave_corrected)
    
    return ave_corrected

def exclude_empty_data(data, labels):  # data and labels are 2 list with same length
    """
    去除空数据，并按照labels的字母排序
    """
    new_data = []
    new_labels = []

    for i, j in zip (data, labels):
        #print('i', i)
        if any(i):
            new_data.append (i)
            # if st.mean (i) > 1:
            #     ave = int (st.mean (i))
            # else:
            #     ave = round (float (st.mean (i)), 2)
            # ave_list.append (ave)
            # j = j + '(n=' + str (len (i)) + ',ave=' + str (ave) + ')'.format (ave)
            new_labels.append (j)
    #     print(len(new_data))
    #     print(new_labels)
    new_labels, new_data = zip (*sorted (zip (new_labels, new_data)))
    #     new_data = [x for _,x in sorted(zip(Y,X))]
    return new_data, new_labels

def get_technology_material(file_name):
    """
    从file_name中获取数据：'technology'和'material'。
    """
    technologies = []
    materials = []
      
    with open (file_name, encoding='ISO-8859-1') as f:
        reader = csv.DictReader (f)
        for row in reader:
            technologies.append (row['Technology'])
            materials.append (row['Material'])
    
    technologies = [tech.strip() for tech in technologies]
    materials = [mat.strip() for mat in materials]
    technologies = sorted (list (set (technologies))) # exclude repeated values
    materials = sorted (list (set (materials)))
    print (str(len(technologies)), ' categories:', technologies)
    print (str(len(materials)), ' materials:', materials)
    
    return technologies, materials

def get_intensity(technologies, materials, file_name, handle_range_value, year_range=None):
    """
    获取数据值。
    """
    value_list = [] # initail value list
    for i in range (len (materials)):
        value_list.append ([])
          
    for empty in value_list: # initial sub list in value list
        for i in range (len (technologies)):
            empty.append ([])
    with open (file_name, encoding='ISO-8859-1')as f:
        reader = csv.DictReader (f)
        tmp = next(reader)  # pass the title row
        for row in reader:
            
            if (not year_range) or ((int(row['Year'])>=year_range[0]) and (int(row['Year'])<=year_range[1])):
                    #print(int(row['Year']), year_range[0], year_range[1])
                    #print('-----------')
                    try:
                        value = float (row['Intensity']) # row[3]代表第4列，
                    except:
                          #             print(row[3])
                        try:
                            a, b = row['Intensity'].split ('-')
                        except:
                            print('rowintensity',row['Intensity'])
                            a, b = row['Intensity'].split (',')
                        a, b = float(a), float(b)
                        if handle_range_value=='average': # 如何处理2个数？均值还是保留2个数？
                            value = (a+b)/2
                        elif handle_range_value=='2_points':
                            value = [a, b]                       
                        else:
                            raise Exception ('Please select how to handle range_value')
              
                      
                    for material in range (len (materials)):
                          
                        sub_value = value_list[material]
                        if row['Material'] == materials[material]:
                            for i, tech in enumerate (technologies):
                                if row['Technology'] == tech:
                                    if isinstance (value, float):
                                        sub_value[i].append (value)
                                    else:
                                        sub_value[i].append (value[0])
                                        sub_value[i].append (value[1])
    print('value list', value_list)
    return value_list

def sorted_by_max(value_list, materials):
    """
    按照最大值排序
    
    """
    max_nb_list = []
    for value in value_list:
        print(value)
        tmp = []
        for i in value:
            for j in i:
                tmp.append(j)
        max_nb = max(tmp)
        max_nb_list.append(max_nb)
     
    ave_list = []  # 存储每个技术的均值
    c_ave_list = []
    
    up_list = []
    down_list = []
    for index, intensity_value in enumerate(value_list):
        c_ave_list.append([])
        ave_list.append([])
        up_list.append([])
        down_list.append([])
        for value in intensity_value:
            if not value: 
                value = [0]
            print(value)
            up = max(value)
            down = min(value)
            print('up', up)
            print('down', down)
            
            up_list[index].append(up)
            down_list[index].append(down)
            
            ave = st.mean(np.array(value))  # 普通求均值                
            ave_list[index].append(ave) #把普通均值存进来
            
            c_ave = correct_ave(value)  # 抛弃异常点再求均值
            c_ave_list[index].append(c_ave) # 同上


            
    max_nb_list, value_list, materials, ave_list, c_ave_list, up_list, down_list = zip(*sorted(zip(max_nb_list, value_list, materials, ave_list, c_ave_list, up_list, down_list), reverse = True))

    return max_nb_list, value_list, materials, ave_list, c_ave_list, up_list, down_list
      

def write_excel(materials, ave_list, c_ave_list, up_list, down_list, file_name, year_range):
    range_list = []
    length = len(up_list[0])
    for i in range(length):
        range_list.append([])

    for down, up in zip(down_list, up_list):
        for n in range(length):
            range_list[n].append([])
            range_list[n][-1].append(down[n])
            range_list[n][-1].append(up[n])
            
    range_dict = {}
    for n in range(length):
        range_dict['range_'+str(n+1)] = range_list[n]
        
    ave_seperated_list = []
    for n in range(length):
        ave_seperated_list.append([])
        for ave in ave_list:
            ave_seperated_list[-1].append(ave[n])
            
    ave_dict = {}
    for n in range(length):
        range_dict['ave_'+str(n+1)] = ave_seperated_list[n]
        

    c_ave_seperated_list = []
    for n in range(length):
        c_ave_seperated_list.append([])
        for c_ave in c_ave_list:
            c_ave_seperated_list[-1].append(c_ave[n])
            
    c_ave_dict = {}
    for n in range(length):
        range_dict['c_ave_'+str(n+1)] = ave_seperated_list[n]

        
    pdf_dict = {'material': materials}
    
    pdf_dict.update(ave_dict)
    pdf_dict.update(c_ave_dict)
    pdf_dict.update(range_dict)
    pdf = pd.DataFrame(pdf_dict)
    #print(pdf)
    #compare_file_name = file_name.split('.csv')[0]+'_compare_'+str(year_range[0])+'_'+str(year_range[1])+'.xlsx'
    #if compare_file_name=='_compare.xlsx':
       #compare_file_name = file_name.split('.xlsx')[0]+'_compare_'+str(year_range[0])+'_'+str(year_range[1])+'.xlsx'
        
    #pdf.to_excel(compare_file_name)
        
if __name__=='__main__':

    technology, materials = get_technology_material(file_name) # 获取技术和材料的名字
    
    intensity_list = get_intensity(technology, materials, file_name, handle_range_value, year_range=year_range) # 获取intensity值
    
    
    intensity_list, materials = exclude_empty_data(intensity_list, materials) # 去掉那些intensity为空的材料
    
    max_nb_list, intensity_list, materials, ave_list, c_ave_list, up_list, down_list = sorted_by_max(intensity_list, materials) 
    
    write_excel(materials, ave_list, c_ave_list, up_list, down_list, file_name, year_range)
     
    for material,max_nb, ave, c_ave, up, down,  value in zip(materials, max_nb_list, ave_list, c_ave_list, up_list, down_list, intensity_list):
        print('-----material,  ave, c_ave, up,down, value-------')
        print(material, ave, c_ave, up, down, value)
        
                
#        print(compare_file_name)
#        with open(compare_file_name, 'a+') as f:
#            writer = csv.writer(f)
#            writer.writerow(material)
            
    
    # plt.figure()
    fig, ax1 = plt.subplots (figsize=(10, 6))
    plt.rcParams['figure.dpi'] = 300
    plt.autoscale()
    flierprops = dict (marker='o', markersize=1, linewidth=0.1, markeredgecolor=cgray)
    meanpointprops = dict(marker='^', markeredgecolor='black', markersize = 0.2, markerfacecolor='black')
    medianprops = dict(color='#000000') #中位数属性
    ax = axes ()
    # hold(True)
    if len(technology)==2:
        color = ['#d8b365', '#5ab4ac']
        
        i, j = 1, 2
        for value, m in zip (intensity_list, materials):
            #flierprops = dict (marker='o', markersize=4)
            bp = boxplot (value, positions=[i, j], widths=0.8, flierprops=flierprops, medianprops=medianprops, meanprops=meanpointprops, patch_artist=True, meanline=False, showmeans=True)
            plt.plot ([j + 1, j + 1], [0, 1000000], color='gray', linestyle='dashed', linewidth=0.5, markersize=1)
            setBoxColors_1 (bp, color=color)
            i, j = i + 3, j + 3
            # draw temporary red and blue lines and use them to create a legend
            hB, = plot ([1, 1],  color=color[0])
            hR, = plot ([1, 1],  color=color[1])
            legend ((hB, hR), (technology[0], technology[1]))
            hB.set_visible (False)
            hR.set_visible (False)
        yscale ('log')
        ylim ((0, 1000000))
        xlim ((0, len(materials)*3))

        new_materials = []
        for i in range (len (materials)):
            new_materials.append (materials[i])
            new_materials.append ('')
        ticks = []
        for i in range (len (new_materials)):
            ticks.append (1.5 * (i + 1))
        plt.xticks (ticks, new_materials, rotation=30, fontsize=10)
        plt.ylabel ('Metal intensity (T/GW)')
        plt.tight_layout ()
        if isinstance(year_range, list):
            savefig ('dd_geared_year_'+str(year_range[0])+'-'+str(year_range[1])+'.png', dpi=dpi)
        else:
            savefig ('dd_geared.png', dpi=dpi)
        show ()
    
    
    elif len(technology)==3:
        color = ['#a6611a', '#dfc27d', '#018571']
        i, j, k = 1, 2, 3
        for value, m in zip (intensity_list, materials):
            #flierprops = dict (marker='o', markersize=4)
            bp = boxplot (value, positions=[i, j, k], widths=0.85, flierprops=flierprops, medianprops=medianprops, meanprops=meanpointprops, patch_artist=True, meanline=False, showmeans=True)
            plt.plot ([k + 1, k + 1], [0, 1000000], color='gray', linestyle='dashed', linewidth=0.5
                      )
            setBoxColors_3 (bp, color=color)
            i, j, k = i + 4, j + 4, k + 4
            # draw temporary red and blue lines and use them to create a legend
            # 下面是设置图例
            hB, = plot ([1, 1], color=color[0])
            hR, = plot ([1, 1], color=color[1])
            hK, = plot ([1, 1], color=color[2])
            legend ((hB, hR, hK), (technology[0], technology[1], technology[2]))
            hB.set_visible (False)
            hR.set_visible (False)
            hK.set_visible (False)
        plt.yscale ('log')
        plt.ylim (0.1, 1000000)
        plt.xlim ((0, len(materials)*4))
    
        new_materials = []
        for i in range (len (materials)):
            new_materials.append (materials[i])
            # new_materials.append ('')
            # new_materials.append ('')
        ticks = []
        print(len(new_materials))
        for i in range (len (materials)):
            ticks.append (4* (i + 1) - 2)
        plt.xticks (ticks, new_materials, rotation=45, fontsize=12)
        plt.ylabel ('Metal intensity (T/GW)')
        plt.tight_layout ()
        
        if isinstance(year_range, list):
            savefig ('on_off_year_'+str(year_range[0])+'-'+str(year_range[1])+'.png', dpi=dpi)
        else:
            savefig ('on_off.png', dpi=dpi)
    
        show ()
    
    
    elif len(technology)==4:
        color = ['red', 'blue', 'green', 'orange']
        h, i, j, k = 1, 2, 3, 4
        for value, m in zip (intensity_list, materials):
            bp = boxplot (value, positions=[h, i, j, k], widths=0.6, flierprops=flierprops, medianprops=medianprops, meanprops=meanpointprops, patch_artist=True)
            plt.plot ([k + 1, k + 1], [0, 1000000], color='gray', linestyle='dashed', linewidth=0.5, markersize=1)
            setBoxColors_1 (bp)
            h, i, j, k = h + 5, i + 5, j + 5, k + 5
            # draw temporary red and blue lines and use them to create a legend
            hB, = plot ([1, 1], 'b-')
            hR, = plot ([1, 1], 'r-')
            hG, = plot ([1, 1], 'g-')
            hK, = plot ([1, 1], 'k-')
            legend ((hB, hR, hG, hK), (technology[0], technology[1], technology[2], technology[3]))
            hB.set_visible (False)
            hR.set_visible (False)
            hG.set_visible (False)
            hK.set_visible (False)
        yscale ('log')
        ylim ((0, 1000000))
        xlim ((0, len(materials)*5))
    
        new_materials = []
        for i in range (len (materials)):
            new_materials.append (materials[i])
            new_materials.append ('')
            new_materials.append ('')
            new_materials.append ('')
        ticks = []
        for i in range (len (new_materials)):
            ticks.append (1.5 * (i + 1))
        plt.xticks (ticks, new_materials, rotation=30, fontsize=9)
        plt.ylabel ('Metal intensity (T/GW)')
        plt.tight_layout ()
        savefig ('***.png', dpi=dpi)
        show ()
        
    
    elif len(technology)==5:
        color = ['#8c510a', '#bf812d', '#dfc27d', '#80cdc1', '#01665e']
        #edge_color = '#084081'
        h, i, j, k, l= 1, 2, 3, 4, 5
        for value, m in zip (intensity_list, materials):
            #flierprops = dict (marker='o', markersize=4)
            bp = boxplot (value, positions=[h, i, j, k, l], widths=1, flierprops=flierprops, medianprops=medianprops,  meanprops=meanpointprops, patch_artist=True, meanline=False, showmeans=True)
            plt.plot ([l + 1, l + 1], [0, max(max_nb_list)*10], color='gray', linestyle='dashed', linewidth=0.5, markersize=1.5)
            setBoxColors_5 (bp,color=color)
            h, i, j, k, l = h + 6, i + 6, j + 6, k + 6, l + 6
            # draw temporary red and blue lines and use them to create a legend
            hB, = plot ([1, 1], color=color[0])
            hR, = plot ([1, 1], color=color[1])
            hG, = plot ([1, 1], color=color[2])
            hO, = plot ([1, 1], color=color[3])
            hC, = plot ([1, 1], color=color[4])
            legend ((hB, hR, hG, hO, hC), (technology[0], technology[1], technology[2], technology[3], technology[4]))
            hB.set_visible (False)
            hR.set_visible (False)
            hG.set_visible (False)
            hO.set_visible (False)
            hC.set_visible (False)
        yscale ('log')
        ylim ((0.5, max(max_nb_list)*10))
        xlim ((0, len(materials)*6))
        new_materials = []
        for i in range (len (materials)):
            
            new_materials.append ('')
            new_materials.append ('')
            new_materials.append (materials[i])#表示横轴元素的位置
            new_materials.append ('')
            new_materials.append ('')
            new_materials.append ('')
        ticks = []
        for i in range (len (new_materials)):
            ticks.append (1 * (i + 1))
        plt.xticks (ticks, new_materials, rotation=45, fontsize=12)
        plt.ylabel ('Metal intensity (T/GW)')
        plt.tight_layout ()
        
        
        if isinstance(year_range, list):
            figname = 'pv_year_'+str(year_range[0])+'-'+str(year_range[1])+'.png'
            savefig (figname, dpi=dpi)
        else:
            savefig ('pv.png', dpi=dpi)
    
        show ()
    # # set axes limits and labels
    # xlim(0,9)
    # ylim(0,9)
    # ax.set_xticklabels(['A', 'B', 'C'])
    # ax.set_xticks([1.5, 4.5, 7.5])
    
    
    
    
    
    
    # randomDists = ['Normal(1,1)', ' Lognormal(1,1)', 'Exp(1)', 'Gumbel(6,4)',
    #                'Triangular(2,9,11)']
    # xtickNames = plt.setp (ax1, xticklabels=np.repeat (randomDists, 2))
    # plt.setp (xtickNames, rotation=45, fontsize=8)
    

