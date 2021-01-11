#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER: Diego Bonilla
# DATE CREATED: 09 Jan 2021                      
# REVISED DATE: 
# PURPOSE: Create a function calculates_results_stats that calculates the 
#          statistics of the results of the programrun using the classifier's model 
#          architecture to classify the images. This function will use the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best' 
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Intro to Python - Project
#          classifying Images - xx Calculating Results" for details on the 
#          how to calculate the counts and percentages for this function.    
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats 
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results statistics 
#          (either a percentage or a count) where the key is the statistic's 
#           name (starting with 'pct' for percentage or 'n' for count) and value 
#          is the statistic's value.  This dictionary should contain the 
#          following keys:
#            n_images - number of images
#            n_dogs_img - number of dog images
#            n_notdogs_img - number of NON-dog images
#            n_match - number of matches between pet & classifier labels
#            n_correct_dogs - number of correctly classified dog images
#            n_correct_notdogs - number of correctly classified NON-dog images
#            n_correct_breed - number of correctly classified dog breeds
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs
#
##
# TODO 5: Define calculates_results_stats function below, please be certain to replace None
#       in the return statement with the results_stats_dic dictionary that you create 
#       with this function
# 
def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the previous topic Calculating Results in the class for details
                     on how to calculate the counts and statistics.
    """        
    # Replace None with the results_stats_dic dictionary that you created with 
    # this function 
    results_stats_dic = {}
    
    # Z: Number of Images
    # length of results_dic, because filenames = key
    total_images = len(results_dic)
    not_dog_images = 0
    results_stats_dic['n_correct_dogs'] = 0
    results_stats_dic['n_dogs_img'] = 0        
    results_stats_dic['n_correct_notdogs'] = 0
    results_stats_dic['n_correct_breed'] = 0 
    results_stats_dic['n_match'] = 0
    
    i = 0
    for key, val in results_dic.items():
#         print(key)
#         print(val)
        
#         if i > 3:
#             break
            
#         i += 1
        
#         pass

        #         A: Number of Correct Dog matches
        #            Both labels are of dogs: results_dic[key][3] = 1 and results_dic[key][4] = 1
        if results_dic[key][3] == 1 and results_dic[key][4] == 1:
            results_stats_dic['n_correct_dogs'] += 1

        #         B: Number of Dog Images
        #            Pet Label is a dog: results_dic[key][3] = 1
        if results_dic[key][3] == 1:
            results_stats_dic['n_dogs_img'] += 1

        #         C: Number of Correct Non-Dog matches
        #            Both labels are NOT of dogs: results_dic[key][3] = 0 and results_dic[key][4] = 0
        if results_dic[key][3] == 0 and results_dic[key][4] == 0:
            results_stats_dic['n_correct_notdogs'] += 1

        # D: Number of Not Dog Images
        # number images - number dog images --OR--
        # Pet Label is NOT a dog: results_dic[key][3] = 0
        #             not_dog_images += 1

        #         E: Number of Correct Breed matches
        #            Pet Label is a dog & Labels match: results_dic[key][3] = 1 and results_dic[key][2] = 1
        if results_dic[key][3] == 1 and results_dic[key][2] == 1:
            results_stats_dic['n_correct_breed'] += 1 

        #         (Optional) Y: Number of label matches
        #            Labels match: results_dic[key][2] = 1
        if results_dic[key][2] == 1:
            results_stats_dic['n_match'] += 1


    # ------------------

    # calculates number of total images
    results_stats_dic['n_images'] = len(results_dic)
    
    # calculates number of not-a-dog images using - images & dog images counts
    results_stats_dic['n_notdogs_img'] = (results_stats_dic['n_images'] - results_stats_dic['n_dogs_img']) 

    # TODO: 5c. REPLACE zero(0.0) with CODE that calculates the % of correctly
    #           matched images. Recall that this can be calculated by the
    #           number of correctly matched images ('n_match') divided by the 
    #           number of images('n_images'). This result will need to be 
    #           multiplied by 100.0 to provide the percentage.
    #    
    # Calculates % correct for matches
    # ------------------
    # (Optional): Percentage Label Matches ( regardless if they're a dog)

    #     Y Number of label matches
    #     Z Number of images
    #   Percentage of correctly Matched Images ( regardless if they are a dog): Y/Z * 100
    pct_label_matches = 0
    if total_images > 0:
        pct_label_matches = results_stats_dic['n_match'] / total_images * 100
    
    results_stats_dic['pct_match'] = pct_label_matches

    # TODO: 5d. REPLACE zero(0.0) with CODE that calculates the % of correctly
    #           classified dog images. Recall that this can be calculated by 
    #           the number of correctly classified dog images('n_correct_dogs')
    #           divided by the number of dog images('n_dogs_img'). This result 
    #           will need to be multiplied by 100.0 to provide the percentage.
    #    
    # ------------------
    # Objective _1_a: Percentage of Correctly Classified Dog Images

    #     A Correctly classified dog images.
    #     B Number of dog images
    #     Percentage of correctly classified "dog" images: A/B * 100
    pct_correct_dogs = 0
    if results_stats_dic['n_dogs_img'] > 0:
        pct_correct_dogs = results_stats_dic['n_correct_dogs'] / results_stats_dic['n_dogs_img'] * 100
    # Calculates % correct dogs
    results_stats_dic['pct_correct_dogs'] = pct_correct_dogs
    
    # Calculates % correct not-a-dog images
    # Uses conditional statement for when no 'not a dog' images were submitted 
    # ------------------
    # Objective _1_b: Percentage of Correctly Classified Non-Dog Images

    #     C Correctly classified NOT a dog images.
    #     D Number of NOT a dog images
    #     Percentage of correctly classified "Non-dog" images: C/D * 100
    #     When calculating the percentage of correctly classified Non-Dog Images, 
    #     use a conditional statement to check that D, 
    #     the number of "not-a-dog" images, is greater than zero. 
    pct_correct_non_dogs = 0
    if results_stats_dic['n_notdogs_img'] > 0:
        pct_correct_non_dogs = results_stats_dic['n_correct_notdogs'] / results_stats_dic['n_notdogs_img'] * 100
        
    results_stats_dic['pct_correct_notdogs'] = pct_correct_non_dogs

    # TODO: 5e. REPLACE zero(0.0) with CODE that calculates the % of correctly
    #           classified breeds of dogs. Recall that this can be calculated 
    #           by the number of correctly classified breeds of dog('n_correct_breed') 
    #           divided by the number of dog images('n_dogs_img'). This result 
    #           will need to be multiplied by 100.0 to provide the percentage.
    #    
    # Calculates % correct breed of dog
    # ------------------
    # Objective _2_: Percentage of Correctly Classified Dog Breeds

    #     E Correctly classified as a particular breed of dog images.
    #     B Number of dog images
    #     Percentage of correctly classified Dog Breed images: E/B * 100
    pct_correct_breed = 0
    if results_stats_dic['n_dogs_img'] > 0:
        pct_correct_breed = results_stats_dic['n_correct_breed'] / results_stats_dic['n_dogs_img'] * 100
    
    results_stats_dic['pct_correct_breed'] = pct_correct_breed
        
    return results_stats_dic
