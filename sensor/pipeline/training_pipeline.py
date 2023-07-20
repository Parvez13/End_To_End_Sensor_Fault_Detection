from sensor.entity.config_entity import (TrainingPipelineConfig,
                                        DataIngestionConfig,
                                        DataValidationConfig)
                                        # DataTransformationConfig,
                                        # ModelTrainerConfig,
                                        # ModelEvaluationConfig,
                                        # ModelPusherConfig
                                        # )
from sensor.entity.artifact_entity import (DataIngestionArtifact,
                                        DataValidationArtifact,
                                        DataTransformationArtifact,
                                        ModelTrainerArtifact,
                                        ModelEvaluationArtifact,
                                        ModelPusherArtifact
                                        )
from sensor.exception import SensorException
from sensor.logger import logging
import os,sys
from sensor.components.data_ingestion import DataIngestion
from sensor.components.data_validation import DataValidation
# from sensor.components.data_transformation import DataTransformation
# from sensor.components.model_trainer import ModelTrainer
# from sensor.components.model_evaluation import ModelEvaluation
# from sensor.components.model_pusher import ModelPusher

class TrainingPipeline:


    def __init__(self,training_pipleine_config:TrainingPipelineConfig):
        try:
            self.training_pipleine_config=training_pipleine_config
        except Exception as e:
            raise SensorException(e, sys)


    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            data_ingestion_config =DataIngestionConfig(
                training_pipeline_config=self.training_pipleine_config)
            
            data_ingestion = DataIngestion(data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            return data_ingestion_artifact
        except Exception as e:
            raise SensorException(e, sys)
    
    def start_data_validation(self,data_ingestion_artifact:DataIngestionArtifact)->DataValidationArtifact:
        try:
            data_validation_config = DataValidationConfig(
                training_pipeline_config=self.training_pipleine_config)
            data_validation = DataValidation(data_validation_config=data_validation_config,
             data_ingestion_artifact=data_ingestion_artifact)
            
            return data_validation.initiate_data_validation()
        except Exception as e:
            raise SensorException(e, sys)



    def start(self,):
        try:
            data_ingestion_artifact = self.start_data_ingestion()

            data_validation_artifact = self.start_data_validation(
                data_ingestion_artifact=data_ingestion_artifact)

            # data_transformation_artifact = self.start_data_transformation(
            #     data_validation_artifact=data_validation_artifact
            # )

            # model_trainer_artifact = self.start_model_trainer(data_transformation_artifact=data_transformation_artifact)
            

            # model_eval_artifact = self.start_model_evaluation(data_validation_artifact=data_validation_artifact,
            #                 data_transformation_artifact=data_transformation_artifact,
            #                 model_trainer_artifact=model_trainer_artifact)

            # model_pusher_artifact = self.start_model_pusher(data_transformation_artifact=data_transformation_artifact,
            #                 model_trainer_artifact=model_trainer_artifact)
        except Exception as e:
            raise SensorException(e, sys)