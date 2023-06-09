import os
import sys
from src.components.model_trainer import ModelTrainer
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

if __name__=='__main__':
    obj = DataIngestion()
    train_data_path,test_data_path = obj.initiate_data_ingestion()
    print(train_data_path,test_data_path)

    data_transformation = DataTransformation()
    final_train_array,final_test_array,_ = data_transformation.initiate_data_transformation(train_data_path,test_data_path)
    ## PASSING TRAIN AND TEST DATA PATH RECEIVED FROM DATA INGESTION TO INITIATE_DATA_TRANSFORMATION AS IT TAKES THE FOLLOWING TWO INPUTS
    
    model_trainer = ModelTrainer()
    model_trainer.initiate_model_training(final_train_array,final_test_array)
