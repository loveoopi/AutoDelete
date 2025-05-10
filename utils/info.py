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

API_ID       = int(os.environ.get("API_ID", "20284828"))
API_HASH     = os.environ.get("API_HASH", "a980ba25306901d5c9b899414d6a9ab7")
BOT_TOKEN    = os.environ.get("BOT_TOKEN", "7148114178:AAGpKYE4hsBg7INn0LqPryseKvSrreP_ZSM")
SESSION      = os.environ.get("SESSION", "BQA8vjJaOVSYIzSY6LBopOnWCB7_mwt9zyTlOzAe1hw7icdAJhi2N7V189d3iJLB5b_9xHec2mNWSaoWloVNXIQ_t0A55v_Cq41DhlHB39JFHdKecaYQlDazTXl_lCC6LCYImJtaozMvUObjCFd6E4Yi5WNGOkmmYdfxFFFmVD-5Q01AuJSYKI5n8umh4LCujXOqR9dbTOmjl-4XqI4hGi08Pvd4ogcyIUFgka4UWNQtpWfvVx_wQnols5FMNL-qH_q4Ck5qpVR2EpBZO4J8MbKkppBjo-yWbZ9jZy6Xb3BNcLTslJlBO75P-SwaUnpSK0Mwq8cN_ckehk_yikWc67JQAAAAAbgp_n0A")
TIME         = int(os.environ.get("TIME", 10))
CHATS        = [int(cht) for cht in os.environ.get("CHATS", "").split()]
WHITE_LIST   = [int(wht) for wht in os.environ.get("WHITE_LIST", "").split()]
BLACK_LIST   = [int(blk) for blk in os.environ.get("BLACK_LIST", "").split()]
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://yacan69355:Cw92BrnfAfWQcLvU@cluster0.jh6h6wg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
PORT         = os.environ.get("PORT", "8080")
