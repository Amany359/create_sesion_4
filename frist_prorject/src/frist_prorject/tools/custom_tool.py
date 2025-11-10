from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import yfinance as yf

class StockInfoInput(BaseModel):
    symbol: str = Field(..., description="رمز السهم مثل AAPL أو MSFT")
    duration: str = Field(default="1mo", description="الفترة الزمنية المراد جلب البيانات عنها")

class StockInfoTool(BaseTool):
    name: str = "أداة تحليل الأسهم"
    description: str = "تقوم بجلب آخر بيانات الأسهم من موقع Yahoo Finance لتحليل الأداء السعري."
    args_schema: Type[BaseModel] = StockInfoInput

    def _run(self, symbol: str, duration: str = "1mo") -> str:
        try:
            stock_data = yf.download(symbol, period=duration)
            if stock_data.empty:
                return f"لم يتم العثور على بيانات للسهم {symbol}"

            latest = stock_data.iloc[-1]
            date = stock_data.index[-1].date()

           
            open_price = float(latest['Open'])
            high_price = float(latest['High'])
            low_price = float(latest['Low'])
            close_price = float(latest['Close'])
            volume = int(latest['Volume'])

            return (
    f"تقرير مختصر عن سهم {symbol}:\n"
    f"التاريخ: {date}\n"
    f"سعر الافتتاح: {open_price:.2f}\n"
    f"أعلى سعر: {high_price:.2f}\n"
    f"أدنى سعر: {low_price:.2f}\n"
    f"سعر الإغلاق: {close_price:.2f}\n"
    f"حجم التداول: {volume}"
)
        except Exception as error:
            return f"حدث خطأ أثناء جلب بيانات السهم: {error}"
