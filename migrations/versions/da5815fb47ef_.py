"""empty message

Revision ID: da5815fb47ef
Revises: 462e5f0b6353
Create Date: 2020-04-28 12:37:28.619048

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'da5815fb47ef'
down_revision = '462e5f0b6353'
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('snow_child',
    sa.Column('id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False, comment='关联的公司用户id'),
    sa.Column('name', mysql.VARCHAR(length=20), nullable=True, comment='测试名字'),
    sa.PrimaryKeyConstraint('id'),
    comment='雪花算法子表',
    mysql_comment='雪花算法子表',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.drop_table('Snow_Child')
    # ### end Alembic commands ###
