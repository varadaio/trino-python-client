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

from typing import Any, Optional


DEFAULT_PORT = 8080
DEFAULT_SOURCE = "trino-python-client"
DEFAULT_CATALOG: Optional[str] = None
DEFAULT_SCHEMA: Optional[str] = None
DEFAULT_AUTH: Optional[Any] = None
DEFAULT_MAX_ATTEMPTS = 3
DEFAULT_REQUEST_TIMEOUT: float = 30.0

HTTP = "http"
HTTPS = "https"

URL_STATEMENT_PATH = "/v1/statement"

class Headers:

    @property
    def base(self):
        return f'X-{self.NAME}'

    @property
    def catalog(self):
        return f'{self.base}-Catalog'

    @property
    def schema(self):
        return f'{self.base}-Schema'

    @property
    def source(self):
        return f'{self.base}-Source'

    @property
    def user(self):
        return f'{self.base}-User'

    @property
    def client_info(self):
        return f'{self.base}-Client-Info'

    @property
    def session(self):
        return f'{self.base}-Session'

    @property
    def set_session(self):
        return f'{self.base}-Set-Session'

    @property
    def clear_session(self):
        return f'{self.base}-Clear-Session'

    @property
    def started_transaction_id(self):
        return f'{self.base}-Started-Transaction-Id'

    @property
    def transaction(self):
        return f'{self.base}-Transaction-Id'

    @property
    def prepared_statement(self):
        return f'{self.base}-Prepared-Statement'

    @property
    def added_prepare(self):
        return f'{self.base}-Added-Prepare'

    @property
    def deallocated_prepare(self):
        return f'{self.base}-Deallocated-Prepare'


class PrestoHeaders(Headers):
    NAME = 'Presto'


class TrinoHeaders(Headers):
    NAME = 'Trino'


def get_headers(presto_headers=False):
    return PrestoHeaders() if presto_headers else TrinoHeaders()