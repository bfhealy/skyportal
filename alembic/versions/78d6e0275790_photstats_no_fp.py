"""photstats_no_fp

Revision ID: 78d6e0275790
Revises: 14b7c22343de
Create Date: 2023-07-05 11:29:54.665460

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78d6e0275790'
down_revision = '14b7c22343de'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        'photstats',
        sa.Column(
            'num_det_no_forced_phot_global',
            sa.Integer(),
            nullable=False,
            server_default='0',
        ),
    )
    op.add_column(
        'photstats',
        sa.Column('first_detected_no_forced_phot_mjd', sa.Float(), nullable=True),
    )
    op.add_column(
        'photstats',
        sa.Column('first_detected_no_forced_phot_mag', sa.Float(), nullable=True),
    )
    op.add_column(
        'photstats',
        sa.Column('first_detected_no_forced_phot_filter', sa.String(), nullable=True),
    )
    op.add_column(
        'photstats',
        sa.Column('last_detected_no_forced_phot_mjd', sa.Float(), nullable=True),
    )
    op.add_column(
        'photstats',
        sa.Column('last_detected_no_forced_phot_mag', sa.Float(), nullable=True),
    )
    op.add_column(
        'photstats',
        sa.Column('last_detected_no_forced_phot_filter', sa.String(), nullable=True),
    )
    op.create_index(
        op.f('ix_photstats_first_detected_no_forced_phot_filter'),
        'photstats',
        ['first_detected_no_forced_phot_filter'],
        unique=False,
    )
    op.create_index(
        op.f('ix_photstats_first_detected_no_forced_phot_mag'),
        'photstats',
        ['first_detected_no_forced_phot_mag'],
        unique=False,
    )
    op.create_index(
        op.f('ix_photstats_first_detected_no_forced_phot_mjd'),
        'photstats',
        ['first_detected_no_forced_phot_mjd'],
        unique=False,
    )
    op.create_index(
        op.f('ix_photstats_last_detected_no_forced_phot_filter'),
        'photstats',
        ['last_detected_no_forced_phot_filter'],
        unique=False,
    )
    op.create_index(
        op.f('ix_photstats_last_detected_no_forced_phot_mag'),
        'photstats',
        ['last_detected_no_forced_phot_mag'],
        unique=False,
    )
    op.create_index(
        op.f('ix_photstats_last_detected_no_forced_phot_mjd'),
        'photstats',
        ['last_detected_no_forced_phot_mjd'],
        unique=False,
    )
    op.create_index(
        op.f('ix_photstats_num_det_no_forced_phot_global'),
        'photstats',
        ['num_det_no_forced_phot_global'],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        op.f('ix_photstats_num_det_no_forced_phot_global'), table_name='photstats'
    )
    op.drop_index(
        op.f('ix_photstats_last_detected_no_forced_phot_mjd'), table_name='photstats'
    )
    op.drop_index(
        op.f('ix_photstats_last_detected_no_forced_phot_mag'), table_name='photstats'
    )
    op.drop_index(
        op.f('ix_photstats_last_detected_no_forced_phot_filter'), table_name='photstats'
    )
    op.drop_index(
        op.f('ix_photstats_first_detected_no_forced_phot_mjd'), table_name='photstats'
    )
    op.drop_index(
        op.f('ix_photstats_first_detected_no_forced_phot_mag'), table_name='photstats'
    )
    op.drop_index(
        op.f('ix_photstats_first_detected_no_forced_phot_filter'),
        table_name='photstats',
    )
    op.drop_column('photstats', 'last_detected_no_forced_phot_filter')
    op.drop_column('photstats', 'last_detected_no_forced_phot_mag')
    op.drop_column('photstats', 'last_detected_no_forced_phot_mjd')
    op.drop_column('photstats', 'first_detected_no_forced_phot_filter')
    op.drop_column('photstats', 'first_detected_no_forced_phot_mag')
    op.drop_column('photstats', 'first_detected_no_forced_phot_mjd')
    op.drop_column('photstats', 'num_det_no_forced_phot_global')
    # ### end Alembic commands ###
