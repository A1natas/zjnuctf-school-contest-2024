use incident;
CREATE TABLE victims
(
    year int(4) NOT NULL AUTO_INCREMENT,
    dead varchar(20) NOT NULL,
    missing varchar(20) NOT NULL,
    PRIMARY KEY (year)
);
INSERT INTO incident.victims (year, dead, missing) VALUES
    ('1979', '大坝监督', '凶手'),
    ('1980', '沙都子继父', '沙都子母亲'),
    ('1981', '古手神社神主', '梨花母亲'),
    ('1982', '北条玉枝', '北条悟史'),
    ('1983', '????', '????');
use s3crets;
CREATE TABLE flag
(
    year int(4)NOT NULL AUTO_INCREMENT,
    flag varchar(100) NOT NULL,
    PRIMARY KEY (year)
);
INSERT INTO s3crets.flag (year, flag) VALUES
    ('1984', 'flag在/flag');