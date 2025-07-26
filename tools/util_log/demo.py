import sys

from loguru import logger

from tools import settings
from tools.util_time import demo

LOG_FILE = settings.LOG_DIR.joinpath(f'{demo.get_now('date')}_viper.log')

logger.remove()

logger.add(
    LOG_FILE,
    rotation='50MB',
    # retention=1,  # 只保留1个日志文件
    format='{time:YYYY-MM-DD HH:mm:ss.SSS} - {level} - {message}',  # 日志格式
    encoding='utf-8',
    enqueue=True,  # 启用异步日志处理
    level='INFO',
    diagnose=False,  # 关闭变量值
    backtrace=False,  # 关闭完整堆栈跟踪
    colorize=False
)

if settings.DEV_MODE:
    logger.add(
        sink=sys.stdout,  # 输出到标准输出流
        format='{time:YYYY-MM-DD HH:mm:ss.SSS} - {level} - {message}',
        enqueue=True,
        level='DEBUG',
        diagnose=False,
        backtrace=False,
        colorize=False
    )
