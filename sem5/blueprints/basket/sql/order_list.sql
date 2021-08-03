select item_id, name, description, price, total
from joom.items
where 1
    and total > 0
order by name
