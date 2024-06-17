#=========================================================================
# [AutoDelete - Telegram bot to delete messages after specific time]      
# Copyright (C) 2022 Arunkumar Shibu                       
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#=========================================================================

import os

API_ID       = int(os.environ.get("API_ID", "22894706"))
API_HASH     = os.environ.get("API_HASH", "13c8f765d49c935d2ffd9152f8430f7e")
BOT_TOKEN    = os.environ.get("BOT_TOKEN", "7148114178:AAGpKYE4hsBg7INn0LqPryseKvSrreP_ZSM")
SESSION      = os.environ.get("SESSION", "BQC6kfsABhUpjLg4BUPOk-ot7uV_MX25n370c6mwHvUFp1GMAaJEwYHg_UEl4jTqGtGg0Zm_ijo4UzB8VMUVHCVSEW-6zrPXMu5sWE3tZpamh7isq0pKwdw8IMHpyGCjy35DimhKibNvkUt1Zy9bfABJPIuUhuyTqcP9aGmt3HAyJF3dj7UgdyLwjDcURuZ636UicPqKpYFj1wR2fqvIJwCsVcEkh0DQmYsQrhN_kthgde6OWU_4wponGLG2-6cftFwvFX_HziYSGhCK4YisiJcY6lOZcQ4jPxRD9ENsMHrEtst_lK7NkXCGdJ_I4ZHxcbvKebOMenENtJOBvaI4c-fG7GGCCwAAAAGnUoSaAA")
TIME         = int(os.environ.get("TIME", 10))
CHATS        = [int(cht) for cht in os.environ.get("CHATS", "").split()]
WHITE_LIST   = [int(wht) for wht in os.environ.get("WHITE_LIST", "").split()]
BLACK_LIST   = [int(blk) for blk in os.environ.get("BLACK_LIST", "").split()]
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Kingrr:4qGUNmnLghYtCQRc@cluster0.s5ezh5y.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
PORT         = os.environ.get("PORT", "8080")
