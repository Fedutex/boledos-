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
import proto  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v8.enums",
    marshal="google.ads.googleads.v8",
    manifest={"BrandSafetySuitabilityEnum",},
)


class BrandSafetySuitabilityEnum(proto.Message):
    r"""Container for enum with 3-Tier brand safety suitability
    control.
        """

    class BrandSafetySuitability(proto.Enum):
        r"""3-Tier brand safety suitability control."""
        UNSPECIFIED = 0
        UNKNOWN = 1
        EXPANDED_INVENTORY = 2
        STANDARD_INVENTORY = 3
        LIMITED_INVENTORY = 4


__all__ = tuple(sorted(__protobuf__.manifest))
