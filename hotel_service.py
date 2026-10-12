class HotelService:
    def __init__(self,service_id,name,price,is_free,opening_hours):

        if not type(service_id)==int and service_id > 0:
            raise ValueError("Service ID should be an integer and greater than 0")

        if name== "" :
            raise ValueError("Service Name cannot be empty")

        if price < 0:
            raise ValueError("Service Price cannot be negative")

        if not type(is_free)==bool:
            raise ValueError("is_free should be a boolean")

        if opening_hours == "":
            raise ValueError("Service Opening Hours cannot be empty")


        self.service_id=service_id
        self.name=name
        self.price=price
        self.is_free=is_free
        self.opening_hours=opening_hours
