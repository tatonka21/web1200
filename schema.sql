drop table if exists linkgroup;
create table linkgroup (
  id integer primary key autoincrement,
  title text not null,
  text text
);

drop table if exists links;
create table links (
  id integer primary key autoincrement,
  linkgroupid integer REFERENCES linkgroup(id),
  title text not null,
  link text,
  description text
);

insert into linkgroup values (1, 'Github Projects', 'Various Bitcoin, Odoo, MySQL projects developed with Python and PHP');
insert into linkgroup values (2, 'Odoo', 'Our Odoo modules');

-- insert into links values (1,  1, 'Project Report', 'https://www.odoo.com/apps/modules/8.0/project_report/','easily generate project standard and custom made project reports');
-- insert into links values (50, 2, 'bitcoinlib', 'https://github.com/1200wd/bitcoinlib', 'Compact python Bitcoin library to work with Private and Public Keys, Wallets, Transactions and the Blockchain', '', '');
