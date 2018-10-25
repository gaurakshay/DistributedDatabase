#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Program to parse the catalog and create mongo script"""
import json
import re


def prepare_monitor(line):
    mon_obj = {}
    attr = line.split(',')
    mon_obj['price'] = {}
    mon_obj['shipping_size'] = {}
    mon_obj['product_type'] = attr[0]
    mon_obj['_id'] = int(attr[1])
    mon_obj['price']['regular'] = float(attr[2])
    mon_obj['price']['discount'] = float(attr[3])
    mon_obj['shipping_size']['length'] = float(attr[4])
    mon_obj['shipping_size']['breadth'] = float(attr[5])
    mon_obj['shipping_size']['depth'] = float(attr[6])
    mon_obj['brand'] = attr[7]
    mon_obj['size'] = attr[8]
    mon_obj['type'] = attr[9]
    mon_obj['frequency'] = attr[10]
    mon_obj['resolution'] = attr[11]
    mon_obj['input_lag'] = attr[12]
    #print json.dumps(mon_obj, indent=4)
    return mon_obj


def prepare_television(line):
    tel_obj = {}
    attr = line.split(',', 14)
    tel_obj['price'] = {}
    tel_obj['shipping_size'] = {}
    #tel_obj['resolution'] = {}
    tel_obj['product_type'] = attr[0]
    tel_obj['_id'] = int(attr[1])
    tel_obj['price']['regular'] = float(attr[2])
    tel_obj['price']['discount'] = float(attr[3])
    tel_obj['shipping_size']['length'] = float(attr[4])
    tel_obj['shipping_size']['breadth'] = float(attr[5])
    tel_obj['shipping_size']['depth'] = float(attr[6])
    tel_obj['brand'] = attr[7]
    tel_obj['size'] = attr[8]
    tel_obj['type'] = attr[9]
    tel_obj['three_d'] = attr[10]
    tel_obj['frequency'] = attr[11]
    #tel_obj['resolution']['lines'] = int(re.search(r'[0-9]+', attr[12]).group(0))
    #tel_obj['resolution']['type'] = re.search(r'[a-zA-Z]+', attr[12]).group(0)
    tel_obj['resolution'] = attr[12]
    tel_obj['input_lag'] = attr[13]
    inputs = attr[14][1:-1].split(',') if (len(attr[14]) > 2) else []
    tel_obj['inputs'] = inputs
    #print json.dumps(tel_obj, indent=4)
    return tel_obj


def prepare_desktop(line):
    desk_obj = {}
    attr = line.split(',', 28)
    desk_obj['price'] = {}
    desk_obj['shipping_size'] = {}
    desk_obj['hard_drive'] = {}
    desk_obj['computer_monitor'] = {}
    desk_obj['hard_drive']['hdd_size'] = {}
    desk_obj['product_type'] = attr[0]
    desk_obj['_id'] = int(attr[1])
    desk_obj['price']['regular'] = float(attr[2])
    desk_obj['price']['discount'] = float(attr[3])
    desk_obj['shipping_size']['length'] = float(attr[4])
    desk_obj['shipping_size']['breadth'] = float(attr[5])
    desk_obj['shipping_size']['depth'] = float(attr[6])
    desk_obj['brand'] = attr[7]
    desk_obj['num_cores'] = attr[8]
    desk_obj['screen_size'] = attr[9]
    desk_obj['hard_drive']['brand'] = attr[11]
    desk_obj['hard_drive']['rpm'] = attr[12]
    desk_obj['hard_drive']['hdd_type'] = attr[13]
    desk_obj['hard_drive']['hdd_size']['size'] = int(re.search(r'[0-9]+', attr[14]).group(0))
    desk_obj['hard_drive']['hdd_size']['factor'] = re.search(r'[a-zA-Z]+', attr[14]).group(0)
    desk_obj['hard_drive']['form_factor'] = attr[15]
    desk_obj['hard_drive']['cache_size'] = attr[16]
    desk_obj['hard_drive']['interface'] = attr[17]
    desk_obj['display_type'] = attr[18]
    desk_obj['computer_monitor']['brand'] = attr[20]
    desk_obj['computer_monitor']['size'] = attr[21]
    desk_obj['computer_monitor']['type'] = attr[22]
    desk_obj['computer_monitor']['frequency'] = attr[23]
    desk_obj['computer_monitor']['resolution'] = attr[24]
    desk_obj['computer_monitor']['input_lag'] = attr[25]
    desk_obj['battery_duration'] = attr[26]
    desk_obj['OS'] = attr[27]
    desk_obj['peripherals'] = attr[28][1:-1].split(',') if (len(attr[28]) > 2) else []
    #print json.dumps(desk_obj, indent=4)
    return desk_obj


def prepare_hdd(line):
    hdd_obj = {}
    attr = line.split(',')
    hdd_obj['price'] = {}
    hdd_obj['shipping_size'] = {}
    hdd_obj['product_type'] = attr[0]
    hdd_obj['_id'] = int(attr[1])
    hdd_obj['price']['regular'] = float(attr[2])
    hdd_obj['price']['discount'] = float(attr[3])
    hdd_obj['shipping_size']['length'] = float(attr[4])
    hdd_obj['shipping_size']['breadth'] = float(attr[5])
    hdd_obj['shipping_size']['depth'] = float(attr[6])
    hdd_obj['brand'] = attr[7]
    hdd_obj['rpm'] = attr[8]
    hdd_obj['hdd_type'] = attr[9]
    hdd_obj['hdd_size'] = attr[10]
    hdd_obj['form_factor'] = attr[11]
    hdd_obj['cache_size'] = attr[12]
    hdd_obj['interface'] = attr[13]
    #print json.dumps(hdd_obj, indent=4)
    return hdd_obj


def prepare_camera(line):
    cam_obj = {}
    attr = line.split(',')
    cam_obj['price'] = {}
    cam_obj['shipping_size'] = {}
    cam_obj['product_type'] = attr[0]
    cam_obj['_id'] = int(attr[1])
    cam_obj['price']['regular'] = float(attr[2])
    cam_obj['price']['discount'] = float(attr[3])
    cam_obj['shipping_size']['length'] = float(attr[4])
    cam_obj['shipping_size']['breadth'] = float(attr[5])
    cam_obj['shipping_size']['depth'] = float(attr[6])
    cam_obj['brand'] = attr[7]
    cam_obj['megapixels'] = attr[8]
    cam_obj['sensor_size'] = attr[9]
    cam_obj['max_iso'] = int(attr[10])
    cam_obj['memory_card_type'] = attr[11]
    cam_obj['camera_type'] = attr[12]
    cam_obj['viewfinder_construction'] = attr[13]
    cam_obj['coverage'] = float(attr[14])
    cam_obj['eye_relief'] = attr[15]
    cam_obj['frames_per_second'] = attr[16]
    cam_obj['num_focus_points'] = int(attr[17])
    cam_obj['focal_length'] = float(attr[18])
    cam_obj['min_aperture'] = float(attr[19])
    #print json.dumps(cam_obj, indent=4)
    return cam_obj


def main():
    objects = []
    """Categorizes input and calls appropriate function"""
    with open('catalog.txt', 'r') as file:
        for line in file:
            type = line[0:3]
            if (type == 'com'):
                #print('Computer')
                objects.append(prepare_monitor(line.strip()))
                #continue
            elif (type == 'tel'):
                #print ('Television')
                objects.append(prepare_television(line.strip()))
                #continue
            elif (type == 'des'):
                #print ('Desktop Monitor')
                objects.append(prepare_desktop(line.strip()))
                #continue
            elif (type == 'har'):
                #print ('Hard Drive')
                objects.append(prepare_hdd(line.strip()))
                #continue
            elif (type == 'dig'):
                #print ('Digital Camera')
                objects.append(prepare_camera(line.strip()))
                #continue
            else:
                continue
    #print json.dumps(objects, indent=4)
    file = open('catalogInsertion.js', 'w')
    file.write('db.product.insert(' + json.dumps(objects, indent=4) + ')')
    file.close


#def create_file():
#    with open('catalog.txt', 'r') as infile:
#        with open('camera.txt', 'w') as outfile:
#            lines = []
#            for line in infile:
#                if (line[0:3] == 'dig'):
#                    lines.append(line)
#            outfile.writelines(lines)
#    print ('successful!!!!!!!!!!!!!')

if __name__ == "__main__":
    main()
