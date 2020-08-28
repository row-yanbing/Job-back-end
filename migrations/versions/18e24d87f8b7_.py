"""empty message

Revision ID: 18e24d87f8b7
Revises: 0f57996de730
Create Date: 2020-04-24 12:58:27.298038

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18e24d87f8b7'
down_revision = '0f57996de730'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Snow_Child',
    sa.Column('id', sa.BigInteger(), autoincrement=False, nullable=False, comment='关联的公司用户id'),
    sa.Column('name', sa.String(length=20), nullable=True, comment='测试名字'),
    sa.PrimaryKeyConstraint('id'),
    comment='雪花算法子表'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Snow_Child')
    # ### end Alembic commands ###