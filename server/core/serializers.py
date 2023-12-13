from rest_framework.serializers import Serializer, ModelSerializer, CharField
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password', 'email']


class GetAnswerSerializer(Serializer):

    # EXAMPLE gender = CharField(required=True)

    gender = CharField(required=False)
    """Пол клиента (0 муж, 1 жен)"""

    age = CharField(required=False)
    """Возраст Клиента"""

    reg_region_nm = CharField(required=False)
    """Регион"""

    cnt_tr_all_3m = CharField(required=False)
    """Количество транзакций за последние 3 месяца"""

    cnt_tr_top_up_3m = CharField(required=False)
    """Количество приходных операций за последние 3 месяца"""

    cnt_tr_cash_3m = CharField(required=False)
    """Количество операций выдачи наличных за последние 3 месяца"""

    cnt_tr_buy_3m = CharField(required=False)
    """Количество операций оплаты покупок за последние 3 месяца"""

    cnt_tr_mobile_3m = CharField(required=False)
    """Количество операций оплаты связи за последние 3 месяца"""

    cnt_tr_oil_3m = CharField(required=False)
    """Количество операций оплаты на АЗС за последние 3 месяца"""

    cnt_tr_on_card_3m = CharField(required=False)
    """Количество операций переводов по карте за последние 3 месяца"""

    cnt_tr_service_3m = CharField(required=False)
    """Количество операций оплаты услуг за последние 3 месяца"""

    cnt_zp_12m = CharField(required=False)
    """Количество зарплатных поступлений за 12 месяцев"""

    sum_zp_12m = CharField(required=False)
    """Сумма зарплатных поступлений за 12m"""

    limit_exchange_count = CharField(required=False)
    """Общее количество изменений лимита"""

    max_outstanding_amount_6m = CharField(required=False)
    """Максимальная задолженность по основному долгу за 6 месяцев"""

    avg_outstanding_amount_3m = CharField(required=False)
    """Средняя задолженность по основному долгу за 3 месяца"""

    cnt_dep_act = CharField(required=False)
    """Количество активных срочных депозитов, имеющих текущий остаток более 1000 р"""

    sum_dep_now = CharField(required=False)
    """Текущая общая сумма (в рублях) срочных депозитов"""

    avg_dep_avg_balance_1month = CharField(required=False)
    """Средний баланс по всем депозитам за последний месяц"""

    max_dep_avg_balance_3month = CharField(required=False)
    """Максимальный баланс по всем депозитам за 3 месяца"""

    app_vehicle_ind = CharField(required=False)
    """Наличие авто"""

    app_position_type_nm = CharField(required=False)
    """Уровень занимаемой позиции"""

    visit_purposes = CharField(required=False)
    """Цель последнего посещения офиса"""

    qnt_months_from_last_visit = CharField(required=False)
    """Количество месяцев с прошлого посещения офиса"""

    super_clust = CharField(required=False)
    """Кластер клиента"""


class IssueTokenRequestSerializer(Serializer):
    model = User

    username = CharField(required=True)
    password = CharField(required=True)


class TokenSeriazliser(ModelSerializer):

    class Meta:
        model = Token
        fields = ['key']
