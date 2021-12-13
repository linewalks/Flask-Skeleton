"""empty message

Revision ID: 4de4db963cee
Revises: 
Create Date: 2021-12-13 16:17:38.393934

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4de4db963cee'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('count', sa.BigInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='public'
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('token', sa.String(length=64), nullable=True),
    sa.Column('token_created_time', sa.DateTime(), nullable=True),
    sa.Column('confirmed', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='public'
    )
    op.create_index(op.f('ix_public_users_email'), 'users', ['email'], unique=True, schema='public')
    op.create_table('tokenblacklist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('jti', sa.String(length=36), nullable=False),
    sa.Column('token_type', sa.String(length=10), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('revoked', sa.Boolean(), nullable=False),
    sa.Column('expires', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['public.users.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id'),
    schema='public'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tokenblacklist', schema='public')
    op.drop_index(op.f('ix_public_users_email'), table_name='users', schema='public')
    op.drop_table('users', schema='public')
    op.drop_table('test', schema='public')
    # ### end Alembic commands ###
