#!/bin/bash

sudo systemctl disable pygrd.service
sudo systemctl daemon-relaod
sudo systemctl enable pygrd.service
sudo systemctl start pygrd.service
sudo systemctl status pygrd.service
