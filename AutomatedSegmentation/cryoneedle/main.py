from monai.apps.auto3dseg import AutoRunner
input = "./task.yaml"
max_epochs = 100

train_param = {
    "num_epochs_per_validation": 1,
    "num_images_per_batch": 2,
    "num_epochs": max_epochs,
}

runner = AutoRunner(input=input)
runner.set_training_params(params=train_param)
runner.set_num_fold(num_fold=4)
runner.set_ensemble_method(ensemble_method_name="AlgoEnsembleBestByFold")
runner.run()