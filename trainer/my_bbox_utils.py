def resize_boxes(target):
    """
    resize the bounding boxes according to the image resizing
    """
    for i in range(len(target['boxes'])):
        target['boxes'][i][0] = (512/target['dims'][i][0]) * target['boxes'][i][0]
        target['boxes'][i][1] = (512/target['dims'][i][1]) * target['boxes'][i][1]
        target['boxes'][i][2] = (512/target['dims'][i][0]) * target['boxes'][i][2]
        target['boxes'][i][3] = (512/target['dims'][i][1]) * target['boxes'][i][3]
    return target

def normalize_boxes(target):
    """
    Divide x_min, x_max by width.
    Divide y_min, y_max by heigth.
    """
    for i in range(len(target['boxes'])):
        norm_1 = target['boxes'][i][0]/target['dims'][i][0]
        norm_2 = target['boxes'][i][1]/target['dims'][i][1]
        norm_3 = target['boxes'][i][2]/target['dims'][i][0]
        norm_4 = target['boxes'][i][3]/target['dims'][i][1]
        target['boxes'][i][0] = norm_1
        target['boxes'][i][1] = norm_2
        target['boxes'][i][2] = norm_3
        target['boxes'][i][3] = norm_4
    return target