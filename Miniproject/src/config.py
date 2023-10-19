from argparse import Namespace
hparams = Namespace(**{'experiment_name': 'object_detection',
                       
                       # Task
                       'train_path': '../../data/extracted/train',
                       'val_path': '../../data/extracted/test',
                       'test_path': '../data/2023/test',
                       'output_dir': 'products/',
                       # Network
                       'num_classes': 7, # 6 for classification, automatically set to 1 for regression
                       'pretrained': False,
                       'loggers': 'tensorboard,', # 'tensorboard, wandb, flowml'
                       'log_embeddings': False,
                       # Training
                       'max_epochs': 30,
                       'learning_rate': 1e-3,
                       'batch_size': 48,
                       #'loss': 'mse',
                       'temperature': 0.1,
                       'n_workers':8,
                       'accelerator':'gpu',
                       # Logs
                       
                       
                       }
                       )