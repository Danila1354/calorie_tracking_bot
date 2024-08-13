from .start import register_handlers_start
from .begin import register_handlers_begin
from .admin_handlers import register_handlers_admin
from .food_diary import register_handlers_food_diary
from .survey import register_handlers_survey
from .water_remind import register_handlers_water_remind
from .profile import register_handlers_profile
def register_all_handlers(dp):
    register_handlers_start(dp)
    register_handlers_begin(dp)
    register_handlers_admin(dp)
    register_handlers_food_diary(dp)
    register_handlers_survey(dp)
    register_handlers_water_remind(dp)
    register_handlers_profile(dp)
