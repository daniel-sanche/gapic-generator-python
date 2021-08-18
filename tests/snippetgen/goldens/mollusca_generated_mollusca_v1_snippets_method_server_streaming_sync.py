# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
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
#
# Generated code. DO NOT EDIT!
#
# Snippet for MethodServerStreaming
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install animalia-mollusca


# [START mollusca_generated_mollusca_v1_Snippets_MethodServerStreaming_sync]
from animalia import mollusca_v1


def sample_method_server_streaming():
    """Snippet for method_server_streaming"""

    # Create a client
    client = mollusca_v1.SnippetsClient()

    # Initialize request argument(s)
    my_message = mollusca_v1.MessageWithNesting()
    my_message.message.required_string = "required_string_value"
    my_message.my_int = 656

    request = mollusca_v1.SignatureRequest(
        my_string="my_string_value",
        my_int=656,
        my_bool=True,
        my_message=my_message,
        single_enum="DEFAULT",
    )

    # Make the request
    stream = client.method_server_streaming(request=request)
    for response in stream:
        print("{}".format(response))

# [END mollusca_generated_mollusca_v1_Snippets_MethodServerStreaming_sync]
