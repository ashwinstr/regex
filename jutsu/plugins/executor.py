# executor.py

import sys
import traceback
from io import StringIO

from pyrogram import filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message

from jutsu import sedex, Config

filter_eval = (
    filters.command("eval", prefixes=";") 
    & filters.user([Config.OWNER_ID])
)

@sedex.on_message(filter_eval, group=-3)
@sedex.on_edited_message(filter_eval, group=-3)
async def execute_it(_, message: Message):
    """ execute python code """
    input_ = message.text.split(maxsplit=1)[1] if " " in message.text else None
    if not input_:
        return await message.reply("`Give input...`")
    reply_ = await message.reply("`Eval started...`")
    sys.stdout = code_out = StringIO()
    sys.stderr = code_err = StringIO()
    formatted_code = "".join(["\n    "+i for i in input_.split("\n")])
    try:
        exec(f"async def exec_(_, message):{formatted_code}")
        func_out = await locals().get("exec_")(_, message)
    except Exception:
        func_out = traceback.format_exc()
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__
    output = code_out.getvalue().strip() or code_err.getvalue.strip() or func_out or ""
    await reply_.edit(f"**>** `{input_}`\n\n**>>** `{output}`", parse_mode=ParseMode.MARKDOWN)
   

term_filters = (
    filters.command("term", prefixes=";")
    & filters.user(Config.OWNER_ID)
)


@sedex.on_message(term_filters, group=-4)
@sedex.on_edited_message(term_filters, group=-4)
async def terminator(_, message: Message):
    """ terminal """


