var gulp = require('gulp'),
    uglify = require('gulp-uglifyjs'),
    cssnano = require('gulp-cssnano'),
    rename = require('gulp-rename'),
    concat = require('gulp-concat');

gulp.task('js', function() {
    return gulp.src([
        './application/static/js/jquery.datetimepicker.full.min.js',
        './application/static/js/script.js'
        ])
        .pipe(concat('libs.min.js'))
        .pipe(uglify())
        .pipe(rename({suffix: '.min'}))
        .pipe(gulp.dest('./application/static/js'));
});

gulp.task('css', function() {
    return gulp.src([
        './application/static/css/jquery.datetimepicker.min.css',
        './application/static/css/normalize.css',
        './application/static/css/skeleton.css',
        './application/static/css/style.css'
        ])
        .pipe(concat('styles.css'))
        .pipe(cssnano())
        .pipe(rename({suffix: '.min'}))
        .pipe(gulp.dest('./product/static/css/'));
});
