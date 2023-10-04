create table anniversary (
       aid integer primary key autoincrement,
       aname text not null,
       adate text not null,
       isholiday int not null,
       uid text not null
);