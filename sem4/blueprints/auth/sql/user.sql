select name,
       group_name
from joom.user
where 1
    and login='$login'
    and password='$password'
