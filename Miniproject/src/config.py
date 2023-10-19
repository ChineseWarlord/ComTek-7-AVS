from argparse import Namespace
hparams = Namespace(**{'experiment_name': 'object_detection',
                       
                       # Task
                       'train_path': 'data/train',
                       'output_dir': 'products/',
                       # Network
                       'num_classes': 5,
                       # Training
                       'max_epochs': 5,
                       'learning_rate': 1e-2,
                       'batch_size': 5,
                       #'loss': 'mse',
                       'temperature': 0.1,
                       'n_workers':8,
                       'accelerator':'gpu',
                       'device':'cuda', 
                       # Logs
                       
                       
                       }
                       )