import argparse
import logging
from experiments import *

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    # general
    parser.add_argument('--exp_name', type=str, help='experiment name', choices=experiments)
    parser.add_argument('--epoch', type=int,  help='continue training')
    parser.add_argument('--gpus', type=str,  help='the gpus will be used, e.g "0,1,2,3"')
    parser.add_argument('--lr', type=float, help='Learning rate. '
                                                 'Notes:'
                                                 'Please set new learning rate when resuming training process, '
                                                 'since lr_scheduler cannot save num_update.')

    # parse args
    args = parser.parse_args()
    ctx = [mx.gpu(int(i)) for i in args.gpus.split(',')]

    # logging
    log_file = os.path.join(config.cfg.model.log_prefix, args.exp_name)
    logging.basicConfig(level=logging.INFO, format='%(asctime)s  %(message)s', filename=log_file, filemode='a')
    
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s  %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

    # perform experiment
    eval(args.exp_name)(args.epoch, ctx, args.lr)