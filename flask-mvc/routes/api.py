from flask_restful import Api

# from controllers.users.userLogin import UserLogin
from controllers.admin.register.signup import AdminSignup
from controllers.admin.register.login import AdminLogin
from controllers.admin.vehicle_type.vehicleTypeOperation import VehicleTypeList, AddVehicleType, EditVehicleType
from controllers.admin.fuel_type.fuelTypeOperation import FuelTypeList, AddFuelType, EditFuelType
from controllers.user.register.signup import UserSignup
from controllers.user.register.login import UserLogin


def create_routes(api: Api):

    ########################## Admin.Register ##########################
    api.add_resource(AdminSignup, '/admin/signup')
    api.add_resource(AdminLogin, '/admin/login')

    ########################## Admin.VehicleType ##########################
    api.add_resource(VehicleTypeList, '/vehicle_type_list')
    api.add_resource(AddVehicleType, '/admin/add_vehicle_type')
    api.add_resource(EditVehicleType, '/admin/edit_vehicle_type')

   ########################## Admin.FuelType ##########################
    api.add_resource(FuelTypeList, '/fuel_type_list')
    api.add_resource(AddFuelType, '/admin/add_fuel_type')
    api.add_resource(EditFuelType, '/admin/edit_fuel_type')

  
   ########################## User.Register ##########################
    api.add_resource(UserSignup, '/user/signup')
    api.add_resource(UserLogin, '/user/login')
