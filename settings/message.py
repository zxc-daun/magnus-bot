# импортируем настройки для отражения эмоджи
from .config import KEYBOARD, VERSION, AUTHOR

# ответ пользователю при посещении блока "О магазине"
trading_store = """

<b>Welcome to the Magnus!!!</b>

This application is developed
especially for sales representatives,
as well as for storekeepers,
commercial organizations carrying out
wholesale and retail trade.

Use the Magnus app,
in a convenient intuitive form will be able to
hard work to take an order from a customer.
Magnus will help you place an order
and in a convenient form addresses the storekeeper
firms for further order picking. 

"""
# ответ пользователю при посещении блока "Настройки"
settings = """
<b>Manuals:</b>

<i>Navigation:</i>

-<b>({}) - </b><i>back</i>
-<b>({}) - </b><i>forward</i>
-<b>({}) - </b><i>increase</i>
-<b>({}) - </b><i>decrease</i>
-<b>({}) - </b><i>next</i>
-<b>({}) - </b><i>previous</i>

<i>Special buttons:</i>

-<b>({}) - </b><i>delete</i>
-<b>({}) - </b><i>order</i>
-<b>({}) - </b><i>confirm order</i>

<i>General information:</i>

-<b>bot version: - </b><i>({})</i>
-<b>developer: - </b><i>({})</i>


<b>{}Shokhzod https://t.me/zxcIown</b>

""".format(
    KEYBOARD['<<'],
    KEYBOARD['>>'],
    KEYBOARD['UP'],
    KEYBOARD['DOUWN'],
    KEYBOARD['NEXT_STEP'],
    KEYBOARD['BACK_STEP'],
    KEYBOARD['X'],
    KEYBOARD['ORDER'],
    KEYBOARD['APPLAY'],
    VERSION,
    AUTHOR,
    KEYBOARD['COPY'],
)
# ответ пользователю при добавлении товара в заказ
product_order = """
Selected product:

{}
{}
Cost: {} $

added to order!!!

There are {} units left in stock. 
"""
# ответ пользователю при посещении блока с заказом
order = """

<i>Name:</i> <b>{}</b>

<i>Description:</i> <b>{}</b>

<i>Cost:</i> <b>{} $ for 1 unit</b>

<i>Number of positions:</i> <b>{} units</b> 
"""

order_number = """

<b>Position in the order № </b> <i>{}</i>

"""
# ответ пользователю, когда заказа нет
no_orders = """
<b>No order !!!</b>
"""
# ответ пользователю при подтверждении оформления заказа
applay = """
<b>Your order has been placed !!!</b>

<i>The total order value is:</i> <b>{} $</b>

<i>The total number of positions is:</i> <b>{} units</b>

<b>ORDER SENT TO WAREHOUSE,
FOR ITS PACKAGING !!!</b>
"""
# словарь ответов пользователю
MESSAGES = {
    'trading_store': trading_store,
    'product_order': product_order,
    'order': order,
    'order_number': order_number,
    'no_orders': no_orders,
    'applay': applay,
    'settings': settings
}
