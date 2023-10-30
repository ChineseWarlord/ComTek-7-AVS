from argparse import Namespace
hparams = Namespace(**{'experiment_name': 'object_detection',
                       
                       # Directories
                       'data': 'data/full', #Use when random_split
                       
                       'train_path': 'data/train', #Use for separate datasets
                       'val_path': 'data/test', #Use for separate datasets
                    #    'test_path': 

                       'output_dir': 'products/',

                       # Network
                       'num_classes': 5, #includes background

                       # Training
                       'max_epochs': 20,
                       'learning_rate': 1e-4,
                       'batch_size': 5,
                       'n_workers':8,
                       'device':'cuda',
                       
                       }
                       )