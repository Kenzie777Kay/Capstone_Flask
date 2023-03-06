"""empty message

Revision ID: 4d73d5cd46ba
Revises: 
Create Date: 2023-03-06 14:22:51.662980

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d73d5cd46ba'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(length=150), nullable=True),
    sa.Column('last_name', sa.String(length=150), nullable=True),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('g_auth_verify', sa.Boolean(), nullable=True),
    sa.Column('token', sa.String(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('canning',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('fruit_or_vegetable', sa.String(length=150), nullable=False),
    sa.Column('style_of_pack', sa.String(length=200), nullable=True),
    sa.Column('jar_size', sa.String(length=20), nullable=True),
    sa.Column('one_to_three_thousand_ft', sa.String(length=200), nullable=True),
    sa.Column('three_to_six_thousand_ft', sa.String(length=200), nullable=True),
    sa.Column('over_six_thousand_ft', sa.String(length=200), nullable=True),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('canning')
    op.drop_table('user')
    # ### end Alembic commands ###
