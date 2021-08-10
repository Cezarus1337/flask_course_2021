select name,
       login,
       group_name
from joom.user
where 1
    and name='$username'
