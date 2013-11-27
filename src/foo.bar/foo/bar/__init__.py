# -*- coding: utf-8 -*-
import argparse


def main():
    """
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--argument",help="The command line argument you set", default=None)
    parser.add_argument("--action",  help="An action you can call", action="store_true")

    args = parser.parse_args()

    if args.action:
        if args.argument != None:
            print "You called the action --action with argument "+args.argument
        else:
            print "You called the action --action without an argument"
