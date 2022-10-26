# this trains the multilabel model (it takes about 10 hours on an ok laptop)
from run_model import run_model
run_model(100, "C:/Github/DataAcademy/data")



###############
# this runs live predictions
from run_live_predictions import run_live_predictions
run_live_predictions(camera_path = "C:/Users/dproc/Pictures/Camera Roll/"
                     ,resize_path= "C:/Github/DataAcademy/predictions/predict_me"
                     , prediction_path="C:/Github/DataAcademy/predictions/output/"
                     , model_path= "C:/Github/DataAcademy/data/models/fit_mutlilabel_model.h5"
                     , eigenface_path = "C:/Github/DataAcademy/predictions/eigenfaces"
                     , lookalike_path = "C:/Github/DataAcademy/predictions/celeb_lookalikes/"
                     , lookalike_model_path = "C:/Github/DataAcademy/test_data/models/fit_multiclass_model.h5"
                     ,num_iterations = 5)


#############
# this trains the multiclass classifier
from run_multiclass_model import run_model
run_model(3, label_sample = 100000)
