from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, TIMESTAMP, text, JSON
from sqlalchemy.dialects.mysql import INTEGER

Base = declarative_base()
metadata = Base.metadata
class Student(Base):

    __tablename__ = 'student'

    id = Column(INTEGER(11), primary_key=True)
    enroll = Column(INTEGER(11))
    personal_info = Column(JSON)
    name= Column(String(255))
    created_on = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))


import datetime

# from . import Base
from sqlalchemy.dialects.mysql import INTEGER  # noqa: F401
from sqlalchemy import (  # noqa: F401
    Column,
    String,
    TIMESTAMP,
    Text,
    JSON,
    Date,
    DateTime,
    Boolean,
    Integer,
    Float,
)


class ConsumerProfile(Base):

    __tablename__ = "consumer_profile_master"

    login_id = Column(String(255))
    client_id = Column(String(255), primary_key=True, index=True, unique=True)
    date = Column(Date)

    # CID - consumer identification details
    cluster_col__market = Column(String(255))
    cid_user_login_type = Column(String(255))
    cid_user_login_status = Column(Boolean())
    cid_user_language = Column(String(255))
    cid_repeat_user = Column(Boolean())
    cid_logged_in_type = Column(String(255))

    # ACQ - Acquisition
    acq_age_with_rea = Column(Integer)
    acq_days_since_last_visit = Column(Integer)
    acq_first_visit_timestamp = Column(Date)
    acq_latest_visit_timestamp = Column(Date)

    # CBS - consumer behaviour segment
    cbs_propensity_score = Column(String(255))
    cbs_leads_generated_count = Column(String(255))
    cbs_Recommended_properties = Column(String(255))
    cbs_journey_segment = Column(String(255))
    cbs_price_sensitive_score = Column(String(255))

    # CEP - consumer engagement profile
    cep_first_lead_timestamp = Column(TIMESTAMP)
    cep_hours_to_first_lead = Column(Integer)
    cep_days_to_first_lead = Column(Integer)
    cep_whatsapp_lead = Column(Integer)
    cep_phone_lead = Column(Integer)
    cep_email_lead = Column(Integer)
    cep_total_leads = Column(Integer)

    cep_min_leads_time_diff_seconds = Column(Float)
    cep_max_leads_time_diff_seconds = Column(Float)
    cep_avg_leads_time_diff_seconds = Column(Float)
    cep_median_leads_time_diff_seconds = Column(Float)
    cep_percentile90_leads_time_diff_seconds = Column(Float)

    cep_average_time_per_session_second = Column(Float)
    cep_max_per_session_second = Column(Float)
    cep_min_per_session_second = Column(Float)
    cep_median_per_session_second = Column(Float)
    cep_percentile_90_per_session_second = Column(Float)

    # PDP-property detail page
    pdp_looking_to_type = Column(String(255))

    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(
        DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )


class LoginClientMapping(Base):

    __tablename__ = "login_client_id"

    login_id = Column(String(255))
    client_id = Column(String(255), primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(
        DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )


class ACQSourceMediumStat(Base):

    __tablename__ = "interaction_stats"

    client_id = Column(String(255), primary_key=True, index=True)
    interaction_type = Column(String(255))
    interaction_name = Column(String(255))
    stats_type = Column(String(255))
    stats_value = Column(Float)
    preferred = Column(Boolean)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(
        DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )


class FAPLoanCare(Base):

    __tablename__ = "financial_loancare"

    client_id = Column(String(255), primary_key=True, index=True)
    request_age = Column(String(255))
    employment_status = Column(String(255))
    salary_type = Column(String(255))
    basic_salary = Column(String(255))
    fixed_allowance = Column(String(255))
    monthly_pcb = Column(String(255))
    commission = Column(String(255))
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(
        DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )


class LSPArticle(Base):

    __tablename__ = "lifestyle_profile"

    client_id = Column(String(255), primary_key=True, index=True)
    visit_start_time = Column(String(255))
    article_id = Column(String(255))
    article_title = Column(String(255))
    article_section = Column(String(255))
    article_tag = Column(String(255))
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(
        DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )


class SRPUserDevice(Base):

    __tablename__ = "srp_user_device"

    client_id = Column(String(255), primary_key=True, index=True)
    browser = Column(String(255))
    browser_version = Column(String(255))
    browser_size = Column(String(255))
    operating_system = Column(String(255))
    operating_system_version = Column(String(255))
    is_mobile = Column(Boolean)
    mobile_device_branding = Column(String(255))
    mobile_device_model = Column(String(255))
    mobile_device_info = Column(String(255))
    language = Column(String(255))
    screen_resolution = Column(String(255))
    device_category = Column(String(255))
    app_id = Column(String(255))
    app_installer_id = Column(String(255))
    app_name = Column(String(255))
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(
        DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )


class SRPUserLocation(Base):

    __tablename__ = "srp_user_location"

    client_id = Column(String(255), primary_key=True, index=True)
    continent = Column(String(255))
    sub_continent = Column(String(255))
    country = Column(String(255))
    region = Column(String(255))
    metro = Column(String(255))
    city = Column(String(255))
    latitude = Column(Float)
    longitude = Column(Float)
    network_location = Column(String(255))
    market = Column(String(255))
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(
        DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )


class CEPLeadGenerated(Base):

    __tablename__ = "cep_leads_generated_per_session"

    client_id = Column(String(255), primary_key=True, index=True)
    visit_number = Column(INTEGER)
    lead_generated_count = Column(INTEGER)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(
        DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )


class CEPTimeDiffLeadGenerated(Base):

    __tablename__ = "cep_diff_in_time_leadGen_seconds"

    client_id = Column(String(255), primary_key=True, index=True)
    diff_in_time_leadGen_seconds = Column(Float)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(
        DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )


class CEPTimeOnSite(Base):

    __tablename__ = "cep_time_on_visit"

    client_id = Column(String(255), primary_key=True, index=True)
    visit_number = Column(INTEGER)
    total_time_on_site_second = Column(Float)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(
        DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )


class PDPPropertyView(Base):

    __tablename__ = "pdp_property_view"

    client_id = Column(String(255), primary_key=True, index=True)
    property_type = Column(String(255))
    tier = Column(String(255))
    visit_start_time = Column(Float)
    visit_number = Column(INTEGER)
    listing_id = Column(String(255))
    listing_channel = Column(String(255))
    price = Column(Float)
    location1 = Column(String(255))
    location2 = Column(String(255))
    location3 = Column(String(255))
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(
        DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )


class PDPPropertyViewCount(Base):

    __tablename__ = "pdp_property_view_count"

    client_id = Column(String(255), primary_key=True, index=True)
    listing_id = Column(String(255))
    count = Column(INTEGER)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(
        DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )


class PDPListingTitle(Base):

    __tablename__ = "pdp_listing_title"

    client_id = Column(String(255), primary_key=True, index=True)
    listing_id = Column(String(255))
    title = Column(String(255))
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(
        DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )


class CEPListingEngagementScore(Base):

    __tablename__ = "cep_listing_engagement_score"

    client_id = Column(String(255), primary_key=True, index=True)
    listing_id = Column(String(255))
    ratings = Column(Float)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(
        DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )


class UserPopularLocation(Base):
    __tablename__ = "user_popular_location"

    clientId = Column(String(255), primary_key=True, index=True)
    location_1_id = Column(Integer(), primary_key=True, index=True)
    location_1_name = Column(String(255))
    channel = Column(String(64), primary_key=True, index=True)
    popular_nearby = Column(Text)
    market = Column(String(64))
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(
        DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )


class PopularLocation(Base):
    __tablename__ = "popular_location"

    location_1_id = Column(Integer())
    location_1_name = Column(String(255))
    location_2_id = Column(Integer())
    location_2_name = Column(String(255))
    channel = Column(String(64))
    market = Column(String(64))
    location_target = Column(String(255), primary_key=True, index=True)
    rank = Column(Integer(), primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(
        DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )


class UserRecommendedProperty(Base):
    __tablename__ = "user_recommended_property"

    clientId = Column(String(255), primary_key=True, index=True)
    channel = Column(String(64), primary_key=True, index=True)
    market = Column(String(64), primary_key=True, index=True)
    buildingIdKnown = Column(Text)
    buildingIdRecommended = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(
        DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )


class SimilarProperty(Base):
    __tablename__ = "similar_property"

    buildingId = Column(String(128), primary_key=True, index=True)
    channel = Column(String(64), primary_key=True, index=True)
    market = Column(String(64), primary_key=True, index=True)
    buildingIdRecommended = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(
        DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )


class PopularProperty(Base):
    __tablename__ = "popular_property"

    id = Column(String(128), primary_key=True, index=True)
    channel = Column(String(64))
    market = Column(String(64))
    userCity = Column(String(128))
    rank = Column(Integer)
    buildingId = Column(String(128))
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(
        DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )


class SessionProfile(Base):
    __tablename__ = "session_profile"

    client_id = Column(String(255), primary_key=True, index=True)
    channel = Column(String(64), primary_key=True, index=True)
    market = Column(String(64), primary_key=True, index=True)
    device = Column(String(64), primary_key=True, index=True)
    data = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(
        DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )


