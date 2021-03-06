#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#
# PROGRAMMER: Yusuke Aita
# DATE CREATED: 20201201 (1st Dec. 2020)
# REVISED DATE: 20201229
# PURPOSE: Create a function classify_images that uses the classifier function
#          to create the classifier labels and then compares the classifier
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function
#             and as in_arg.dir for function call within main.
#            -The results dictionary as results_dic within classify_images
#             function and results for the functin call within main.
#            -The CNN model architecture as model wihtin classify_images function
#             and in_arg.arch for the function call within main.
#           This function uses the extend function to add items to the list
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images
from classifier import classifier

# TODO 3: Define classify_images function below, specifically replace the None
#       below by the function definition of the classify_images function.
#       Notice that this function doesn't return anything because the
#       results_dic dictionary that is passed into the function is a mutable
#       data type so no return is needed.
#
def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function,
    compares pet labels to the classifier labels,
    and adds the classifier label and the comparison of
    the labels to the results dictionary using the extend function.

    Be sure to
    format the classifier labels so that they will match your pet image labels.

    The format will include putting the classifier labels in all lower case
    letters and strip the leading and trailing whitespace characters from them.
    For example, the Classifier function returns = 'Maltese dog, Maltese terrier, Maltese'
    so the classifier label = 'maltese dog, maltese terrier, maltese'.

    Recall that dog names from the classifier function can be a string of dog
    names separated by commas when a particular breed of dog has multiple dog
    names associated with that breed. For example, you will find pet images of
    a 'dalmatian'(pet label) and it will match to the classifier label
    'dalmatian, coach dog, carriage dog' if the classifier function correctly
    classified the pet images of dalmatians.

     PLEASE NOTE: This function uses the classifier() function defined in
     classifier.py within this function. The proper use of this function is
     in test_classifier.py Please refer to this program prior to using the
     classifier() function to classify images within this function
     Parameters:
      images_dir - The (full) path to the folder of images that are to be
                   classified by the classifier function (string)
      results_dic - Results Dictionary with 'key' as image filename and 'value'
                    as a List. Where the list will contain the following items:
                  index 0 = pet image label (string)
                --- where index 1 & index 2 are added by this function ---
                  NEW - index 1 = classifier label (string)
                  NEW - index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
      model - Indicates which CNN model architecture will be used by the
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
     Returns:
           None - results_dic is mutable data type so no return needed.
    """

    image_path_list = []

    # test image
    # test_image = "pet_images/Collie_03797.jpg"
    image_path = []

    chosen_model = model

    # Key For Loop
    for k in results_dic:
        # print("Key =", k)
        key_str = str(k)

        image_path = images_dir + key_str
        # print("image_path =", image_path)

        image_classification = classifier(image_path, chosen_model)

        # Extend the list in the value by adding its path with "append"
        # results_dic[k].append(image_path)
        # print("results_dic[k] = ", results_dic[k])

        # test classifier function
        # print("image_classification output:", image_classification)

        # to extract dictionary.items[0]. Here there is only one value in the dictionary
        search_pet_label = results_dic[k]


        # Edit the name of the image_classification
        classified_label = image_classification
        low_classified_label = classified_label.lower()

        results_dic[k].append(low_classified_label)
        # print("results_dic[k] = ", results_dic[k])

        # to extract dictionary.items[0]
        # search_pet_label = results_dic[k]

        # the value of results_dic is substituted for name_comp_value
        name_comp_value = results_dic[k]
        # print("name_comp_value: ", name_comp_value)

        name_comp_list = list(name_comp_value)
        #for i in range(0, len(name_comp_list), 1):
        #    print("name_comp_list is no{}, content = {}".format(i,\
 #                                                               #name_comp_list[i]))
        full_pet_name_comp_list = name_comp_list[0]
        # print("full_pet_name_comp_list is ", full_pet_name_comp_list)

        # split_full_name_comp_list = full_name_comp_list.strip("'/")
        full_label_name_comp_list = name_comp_list[1]
        # print("full_label_name_comp_list is",full_label_name_comp_list)

        if full_pet_name_comp_list in full_label_name_comp_list:
            # print("OK")
            results_dic[k].append(1)
        else:
            # print("NG")
            results_dic[k].append(0)

        # print("(judge) results_dic[k] = ", results_dic[k])

        #word_list_low_classified_label = low_classified_label.split(",")

                # Create its petname from the filename
                #pet_image = filename
                #low_pet_image = pet_image.lower()
                #word_list_pet_image = low_pet_image.split("_")
                #print("type of word_list_pet_image is", type(word_list_pet_image))

                # Create pet_name starting as empty string
                #pet_name = ""
                #print("type of pet_name is", type(pet_name))

                # Loops to check if word in pet_name is only alphabetic characters
                # if true append word to pet_name separated by trailing space
                #for word in word_list_pet_image:
                #    if word.isalpha():
                #        pet_name += word + " "

                # Strip off starting/trailing whitespace characters
                #pet_name = pet_name.strip()

                # Add the pet_name into pet_labels
                #pet_labels.append(pet_name)

        # Reset image_path
        image_path = []

        #results

    # Test to call the contents of the dictionary
    # print("results in classifty_images.py :\ ", results_dic)

    #path_dir = images_dir
    #dic = results_dic

    #path_dir = images_dir
    #dic = results_dic

    None
