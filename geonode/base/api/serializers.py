# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2020 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

from rest_framework import serializers
from dynamic_rest.serializers import DynamicModelSerializer
from dynamic_rest.fields.fields import DynamicRelationField, DynamicComputedField

from geonode.base.models import (
    ResourceBase,
    HierarchicalKeyword,
    Region,
    RestrictionCodeType,
    License,
    TopicCategory,
    SpatialRepresentationType
)

import logging

logger = logging.getLogger(__name__)


class GroupSerializer(DynamicModelSerializer):

    class Meta:
        model = Group
        name = 'group'
        fields = ('pk', 'name')


class UserSerializer(DynamicModelSerializer):

    class Meta:
        model = get_user_model()
        name = 'user'
        # fields = ('pk', 'username', 'email', 'is_superuser', 'is_staff', 'groups')
        fields = ('pk', 'username', 'first_name', 'last_name', 'groups')

    @classmethod
    def setup_eager_loading(cls, queryset):
        """ Perform necessary eager loading of data. """
        queryset = queryset.prefetch_related()
        return queryset

    groups = DynamicRelationField(GroupSerializer, embed=True, many=True)


class ContactRoleField(DynamicComputedField):

    def __init__(self, contat_type, **kwargs):
        self.contat_type = contat_type
        super(ContactRoleField, self).__init__(**kwargs)

    def get_attribute(self, instance):
        return getattr(instance, self.contat_type)

    def to_representation(self, value):
        return UserSerializer(embed=True, many=False).to_representation(value)


class ResourceBaseSerializer(DynamicModelSerializer):

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(ResourceBaseSerializer, self).__init__(*args, **kwargs)

        self.fields['pk'] = serializers.CharField(read_only=True)
        self.fields['uuid'] = serializers.CharField(read_only=True)
        self.fields['owner'] = DynamicRelationField(UserSerializer, embed=True, many=False, read_only=True)
        self.fields['poc'] = ContactRoleField('poc', read_only=True)
        self.fields['metadata_author'] = ContactRoleField('metadata_author', read_only=True)
        self.fields['title'] = serializers.CharField()
        self.fields['abstract'] = serializers.CharField()
        self.fields['doi'] = serializers.CharField()
        self.fields['alternate'] = serializers.CharField(read_only=True)
        self.fields['date'] = serializers.DateTimeField()
        self.fields['date_type'] = serializers.CharField()
        self.fields['temporal_extent_start'] = serializers.DateTimeField()
        self.fields['temporal_extent_end'] = serializers.DateTimeField()
        self.fields['edition'] = serializers.CharField()
        self.fields['purpose'] = serializers.CharField()
        self.fields['maintenance_frequency'] = serializers.CharField()
        self.fields['constraints_other'] = serializers.CharField()
        self.fields['language'] = serializers.CharField()
        self.fields['supplemental_information'] = serializers.CharField()
        self.fields['data_quality_statement'] = serializers.CharField()
        self.fields['bbox_x0'] = serializers.DecimalField(max_digits=30, decimal_places=15)
        self.fields['bbox_x1'] = serializers.DecimalField(max_digits=30, decimal_places=15)
        self.fields['bbox_y0'] = serializers.DecimalField(max_digits=30, decimal_places=15)
        self.fields['bbox_y1'] = serializers.DecimalField(max_digits=30, decimal_places=15)
        self.fields['srid'] = serializers.CharField()
        self.fields['group'] = DynamicRelationField(GroupSerializer, embed=True, many=False)

        self.fields['keywords'] = serializers.SlugRelatedField(
            many=True, slug_field='slug', queryset=HierarchicalKeyword.objects.all())
        self.fields['regions'] = serializers.SlugRelatedField(
            many=True, slug_field='name', queryset=Region.objects.all())
        self.fields['category'] = serializers.SlugRelatedField(
            many=False, slug_field='identifier', queryset=TopicCategory.objects.all())
        self.fields['restriction_code_type'] = serializers.SlugRelatedField(
            many=False, slug_field='identifier', queryset=RestrictionCodeType.objects.all())
        self.fields['license'] = serializers.SlugRelatedField(
            many=False, slug_field='identifier', queryset=License.objects.all())
        self.fields['spatial_representation_type'] = serializers.SlugRelatedField(
            many=False, slug_field='identifier', queryset=SpatialRepresentationType.objects.all())

    class Meta:
        model = ResourceBase
        name = 'resource'
        fields = (
            'pk', 'uuid', 'owner', 'poc', 'metadata_author',
            'title', 'abstract', 'doi', 'alternate',
            'keywords', 'regions', 'category',
            'date', 'date_type', 'edition', 'purpose', 'maintenance_frequency',
            'restriction_code_type', 'constraints_other', 'license', 'language',
            'spatial_representation_type', 'temporal_extent_start', 'temporal_extent_end',
            'supplemental_information', 'data_quality_statement', 'group',
            'bbox_x0', 'bbox_x1', 'bbox_y0', 'bbox_y1', 'srid',
            # TODO
            # csw_typename, csw_schema, csw_mdsource, csw_insert_date, csw_type, csw_anytext, csw_wkt_geometry,
            # metadata_uploaded, metadata_uploaded_preserve, metadata_xml,
            # popular_count, share_count, featured, is_published, is_approved,
            # thumbnail_url, detail_url, rating, created, last_updated, dirty_state,
            # users_geolimits, groups_geolimits
        )
