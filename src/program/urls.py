from django.urls import path, include
from .views import *

app_name = "program"

urlpatterns = [
    path("", ScheduleView.as_view(), name="schedule_index"),
    path("noscript/", NoScriptScheduleView.as_view(), name="noscript_schedule_index"),
    path("ics/", ICSView.as_view(), name="ics_view"),
    path("control/", ProgramControlCenter.as_view(), name="program_control_center"),
    path(
        "proposals/",
        include(
            [
                path("", ProposalListView.as_view(), name="proposal_list"),
                path(
                    "submit/",
                    include(
                        [
                            path(
                                "",
                                CombinedProposalTypeSelectView.as_view(),
                                name="proposal_combined_type_select",
                            ),
                            path(
                                "<slug:event_type_slug>/",
                                CombinedProposalSubmitView.as_view(),
                                name="proposal_combined_submit",
                            ),
                            path(
                                "<slug:event_type_slug>/select_person/",
                                CombinedProposalPersonSelectView.as_view(),
                                name="proposal_combined_person_select",
                            ),
                        ]
                    ),
                ),
                path(
                    "people/",
                    include(
                        [
                            path(
                                "<uuid:pk>/",
                                SpeakerProposalDetailView.as_view(),
                                name="speakerproposal_detail",
                            ),
                            path(
                                "<uuid:pk>/update/",
                                SpeakerProposalUpdateView.as_view(),
                                name="speakerproposal_update",
                            ),
                            path(
                                "<uuid:pk>/delete/",
                                SpeakerProposalDeleteView.as_view(),
                                name="speakerproposal_delete",
                            ),
                            path(
                                "<uuid:speaker_uuid>/add_event/",
                                EventProposalTypeSelectView.as_view(),
                                name="eventproposal_typeselect",
                            ),
                            path(
                                "<uuid:speaker_uuid>/add_event/<slug:event_type_slug>/",
                                EventProposalCreateView.as_view(),
                                name="eventproposal_create",
                            ),
                            path(
                                "<uuid:speaker_uuid>/add_url/",
                                UrlCreateView.as_view(),
                                name="speakerproposalurl_create",
                            ),
                            path(
                                "<uuid:speaker_uuid>/urls/<uuid:url_uuid>/update/",
                                UrlUpdateView.as_view(),
                                name="speakerproposalurl_update",
                            ),
                            path(
                                "<uuid:speaker_uuid>/urls/<uuid:url_uuid>/delete/",
                                UrlDeleteView.as_view(),
                                name="speakerproposalurl_delete",
                            ),
                        ]
                    ),
                ),
                path(
                    "events/",
                    include(
                        [
                            path(
                                "<uuid:pk>/",
                                EventProposalDetailView.as_view(),
                                name="eventproposal_detail",
                            ),
                            path(
                                "<uuid:pk>/update/",
                                EventProposalUpdateView.as_view(),
                                name="eventproposal_update",
                            ),
                            path(
                                "<uuid:pk>/delete/",
                                EventProposalDeleteView.as_view(),
                                name="eventproposal_delete",
                            ),
                            path(
                                "<uuid:event_uuid>/add_person/",
                                EventProposalSelectPersonView.as_view(),
                                name="eventproposal_selectperson",
                            ),
                            path(
                                "<uuid:event_uuid>/add_person/new/",
                                SpeakerProposalCreateView.as_view(),
                                name="speakerproposal_create",
                            ),
                            path(
                                "<uuid:event_uuid>/add_person/<uuid:speaker_uuid>/",
                                EventProposalAddPersonView.as_view(),
                                name="eventproposal_addperson",
                            ),
                            path(
                                "<uuid:event_uuid>/remove_person/<uuid:speaker_uuid>/",
                                EventProposalRemovePersonView.as_view(),
                                name="eventproposal_removeperson",
                            ),
                            path(
                                "<uuid:event_uuid>/add_url/",
                                UrlCreateView.as_view(),
                                name="eventproposalurl_create",
                            ),
                            path(
                                "<uuid:event_uuid>/urls/<uuid:url_uuid>/update/",
                                UrlUpdateView.as_view(),
                                name="eventproposalurl_update",
                            ),
                            path(
                                "<uuid:event_uuid>/urls/<uuid:url_uuid>/delete/",
                                UrlDeleteView.as_view(),
                                name="eventproposalurl_delete",
                            ),
                        ]
                    ),
                ),
            ]
        ),
    ),
    path(
        "speakers/",
        include(
            [
                path("", SpeakerListView.as_view(), name="speaker_index"),
                path(
                    "<slug:slug>/", SpeakerDetailView.as_view(), name="speaker_detail"
                ),
            ]
        ),
    ),
    path("events/", EventListView.as_view(), name="event_index"),
    # legacy CFS url kept on purpose to keep old links functional
    path(
        "call-for-speakers/",
        CallForParticipationView.as_view(),
        name="call_for_speakers",
    ),
    path(
        "call-for-participation/",
        CallForParticipationView.as_view(),
        name="call_for_participation",
    ),
    path("calendar", ICSView.as_view(), name="ics_calendar"),
    # this must be the last URL here or the regex will overrule the others
    path("<slug:slug>/", EventDetailView.as_view(), name="event_detail"),
]
