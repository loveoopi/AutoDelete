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
BOT_TOKEN    = os.environ.get("BOT_TOKEN", "7526341864:AAHY_jubxXuFratDh8XFR2Se4M4oTycjFA4")
SESSION      = os.environ.get("SESSION", "BQE1hZwAmlcn55SBlvXOn2PRhEoitba8X-M05FSoEg-ZUaUHvvgstVtjTCfrxmVYSCBgG1UihZvaPnDkAumhS3VVDsiHT3k0JxUmNnYjm2U9ABTrsCyv4oSkbnnYCdthC9jbtWs4TBsnDSm22T-p5MsryPSAUd17RKcnLVInRDkH1avnKlPwuX3U8Demi7dhfkf4lMbnRPYf-bRHpBvb_1nRW9URfCQKitsJuJDNGyjTuY8vK0hQcsTkFZnhuZ4toGcRhayb0nNKTW70l6mluQpTVy4zm72lmDS1G72FCiqDJ9ayy58ndrN0GJkdfpaZVYfcQY0znw2i6wnOKdoRS6tOEdZBGQAAAAGP_MEgAA")
TIME         = int(os.environ.get("TIME", 10))
CHATS        = [int(cht) for cht in os.environ.get("CHATS", "").split()]
WHITE_LIST   = [int(wht) for wht in os.environ.get("WHITE_LIST", "").split()]
BLACK_LIST   = [int(blk) for blk in os.environ.get("BLACK_LIST", "").split()]
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://yacan69355:Cw92BrnfAfWQcLvU@cluster0.jh6h6wg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
PORT         = os.environ.get("PORT", "8080")
