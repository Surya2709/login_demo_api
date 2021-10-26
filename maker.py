import os



def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)
    app.register_blueprint(user.USER_BLUEPRINT)
    app.register_blueprint(address.ADDRESS_BLUEPRINT)
    app.register_blueprint(business.BUSINESS_BLUEPRINT)
    app.register_blueprint(profile.PROFILE_BLUEPRINT)
    app.register_blueprint(traveller.TRAVELLER_BLUEPRINT)
    app.register_blueprint(ffp.FFP_BLUEPRINT)
    app.register_blueprint(gst.GST_BLUEPRINT)
    app.register_blueprint(ALIVE_SERVICE_BLUEPRINT)
    app.register_blueprint(verify.VERIFY_BLUEPRINT)
    app.register_blueprint(anti_foreign.ANTI_FOREIGN_BLUEPRINT)
    app.register_blueprint(captcha.CAPTCHA_BLUEPRINT)
    app.register_blueprint(user_details.USER_DETAILS_BLUEPRINT)
    app.register_blueprint(user_consent.USER_CONSENT_BLUEPRINT)
    app.register_blueprint(otp_trigger.OTP_TRIGGER_BLUEPRINT)
    app.register_blueprint(public_key.PUBLIC_KEY_BLUEPRINT)
    app.register_blueprint(security_key.SECURITY_KEY_BLUEPRINT)
    app.register_blueprint(referral.REFERRAL_BLUEPRINT)
    app.register_blueprint(version_control.VERSION_CONTROL_BLUEPRINT)
    app.register_error_handler(Exception, handle_error)
    # db.init_app(app)
    # Migrate(app, db)
    return app
