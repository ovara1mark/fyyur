"""empty message

Revision ID: 651ea93259e4
Revises: bdea4fe18d92
Create Date: 2022-05-27 19:42:44.528670

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '651ea93259e4'
down_revision = 'bdea4fe18d92'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('artist', 'website_link',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('artist', 'seeking_venue',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('artist', 'seeking_description',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('artist', 'seeking_description',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('artist', 'seeking_venue',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('artist', 'website_link',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    # ### end Alembic commands ###