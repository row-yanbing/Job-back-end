"""empty message

Revision ID: 0f57996de730
Revises: 722222df86fe
Create Date: 2020-04-24 12:55:26.517501

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0f57996de730'
down_revision = '722222df86fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('snow_test')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('snow_test',
    sa.Column('id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False, comment='关联的公司用户id'),
    sa.Column('name', mysql.VARCHAR(length=20), nullable=True, comment='测试名字'),
    sa.PrimaryKeyConstraint('id'),
    comment='雪花算法基础表',
    mysql_comment='雪花算法基础表',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
