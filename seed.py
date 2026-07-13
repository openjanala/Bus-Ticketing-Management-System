from app import create_app
from app.extensions import db
from app.models.bus_type import BusType

app = create_app()

with app.app_context():

    bus_types = [
        "AC",
        "Non AC",
        "Sleeper",
        "Business"
    ]

    for name in bus_types:

        exists = BusType.query.filter_by(
            type_name=name
        ).first()

        if not exists:

            db.session.add(
                BusType(type_name=name)
            )

    db.session.commit()

    print("Bus Types Inserted Successfully.")