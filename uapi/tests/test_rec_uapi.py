# Copyright (c) 2023 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys

__dir__ = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(__dir__, '..', '..')))

from uapi import PaddleModel

if __name__ == '__main__':
    model = PaddleModel(model_name='ch_PP-OCRv3_rec')

    model.train(
        dataset='uapi/tests/data/ic15_data',
        batch_size=32,
        epochs_iters=1,
        device='gpu:0',
        dy2st=False,
        amp='O2',
        save_dir='uapi/tests/ocr_rec_res')

    model.predict(
        weight_path='uapi/tests/ocr_rec_res/latest.pdparams',
        device='gpu',
        input_path='uapi/tests/data/ic15_data/train/word_1.png',
        save_dir='uapi/tests/ocr_rec_res/pred_res')

    model.export(
        weight_path='uapi/tests/ocr_rec_res/latest.pdparams',
        save_dir='uapi/tests/ocr_rec_res/infer')

    model.infer(
        model_dir='uapi/tests/ocr_rec_res/infer/Student',
        device='gpu',
        input_path='uapi/tests/data/ic15_data/train/word_1.png')

    model.compression(
        dataset='uapi/tests/data/ic15_data',
        batch_size=16,
        learning_rate=0.1,
        epochs_iters=1,
        device='gpu',
        weight_path='uapi/tests/ocr_rec_res/latest.pdparams',
        save_dir='uapi/tests/ocr_rec_res/compress')
