from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger import logging
from housing.config.configuration import Configuartion
from housing.component.data_transformation import  DataTransformation
import os

def main():
    try:

        pipeline = Pipeline()
        pipeline.run_pipeline()

        #data_validation_config = Configuartion().get_data_transformation_config()
        #print(data_validation_config)
        #logging.info("main function execution completed.")
        # # data_validation_config = Configuartion().get_data_transformation_config()
        # # print(data_validation_config)
        #schema_file_path=r"C:\Users\pc\Desktop\FSDS Project\project-deployment-practice\config\schema.yaml"
        #file_path = r"C:\Users\pc\Desktop\FSDS Project\project-deployment-practice\housing\artifact\data_ingestion\2022-07-20-22-51-36\ingested_data\train\housing.csv"
        #df= DataTransformation.load_data(file_path=file_path,schema_file_path=schema_file_path)
        #print(df.columns)
        #print(df.dtypes)

    except Exception as e:
        logging.error(f"{e}")
        print(e)



if __name__=="__main__":
    main()

