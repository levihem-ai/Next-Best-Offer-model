import uuid
from django.db import models


class Dialogs(models.Model):
    dialog_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    gender = models.CharField(max_length=4000)
    """Пол клиента (0 муж, 1 жен)"""

    age = models.CharField(max_length=4000)
    """Возраст Клиента"""

    reg_region_nm = models.CharField(max_length=4000)
    """Регион"""

    cnt_tr_all_3m = models.CharField(max_length=4000)
    """Количество транзакций за последние 3 месяца"""

    cnt_tr_top_up_3m = models.CharField(max_length=4000)
    """Количество приходных операций за последние 3 месяца"""

    cnt_tr_cash_3m = models.CharField(max_length=4000)
    """Количество операций выдачи наличных за последние 3 месяца"""

    cnt_tr_buy_3m = models.CharField(max_length=4000)
    """Количество операций оплаты покупок за последние 3 месяца"""

    cnt_tr_mobile_3m = models.CharField(max_length=4000)
    """Количество операций оплаты связи за последние 3 месяца"""

    cnt_tr_oil_3m = models.CharField(max_length=4000)
    """Количество операций оплаты на АЗС за последние 3 месяца"""

    cnt_tr_on_card_3m = models.CharField(max_length=4000)
    """Количество операций переводов по карте за последние 3 месяца"""

    cnt_tr_service_3m = models.CharField(max_length=4000)
    """Количество операций оплаты услуг за последние 3 месяца"""

    cnt_zp_12m = models.CharField(max_length=4000)
    """Количество зарплатных поступлений за 12 месяцев"""

    sum_zp_12m = models.CharField(max_length=4000)
    """Сумма зарплатных поступлений за 12m"""

    limit_exchange_count = models.CharField(max_length=4000)
    """Общее количество изменений лимита"""

    max_outstanding_amount_6m = models.CharField(max_length=4000)
    """Максимальная задолженность по основному долгу за 6 месяцев"""

    avg_outstanding_amount_3m = models.CharField(max_length=4000)
    """Средняя задолженность по основному долгу за 3 месяца"""

    cnt_dep_act = models.CharField(max_length=4000)
    """Количество активных срочных депозитов, имеющих текущий остаток более 1000 р"""

    sum_dep_now = models.CharField(max_length=4000)
    """Текущая общая сумма (в рублях) срочных депозитов"""

    avg_dep_avg_balance_1month = models.CharField(max_length=4000)
    """Средний баланс по всем депозитам за последний месяц"""

    max_dep_avg_balance_3month = models.CharField(max_length=4000)
    """Максимальный баланс по всем депозитам за 3 месяца"""

    app_vehicle_ind = models.CharField(max_length=4000)
    """Наличие авто"""

    app_position_type_nm = models.CharField(max_length=4000)
    """Уровень занимаемой позиции"""

    visit_purposes = models.CharField(max_length=4000)
    """Цель последнего посещения офиса"""

    qnt_months_from_last_visit = models.CharField(max_length=4000)
    """Количество месяцев с прошлого посещения офиса"""

    super_clust = models.CharField(max_length=4000)
    """Кластер клиента"""

    def __str__(self):
        return f'{self.question} {self.answer}'
